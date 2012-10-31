import gzip
import logging
import operator
import re
import sys
import tempfile
from StringIO import StringIO
from optparse import make_option

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from utility.run import *
from utility.backup import _BACKUP_DUMPFILE_PREFIX, FTP_HOST, FTP_USER, FTP_PASS

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--restore-only',
                    action="store_true",
                    dest="restore_only",
                    default=False),
        )

    def handle(self, *args, **options):
        connection = S3Connection(settings.AWS_ACCESS_KEY_ID,
                                  settings.AWS_SECRET_ACCESS_KEY)
        bucket = connection.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        candidate_list = bucket.list(prefix=_BACKUP_S3_DUMPFILE_PREFIX)
        key_list = map(lambda x: x, candidate_list)
        key_list.sort(key=operator.attrgetter('key'), reverse=True)
        logging.warning('%d candidate dumps found' % len(key_list))
        pattern = re.compile("^%s(\d{14}).gz$" % _BACKUP_S3_DUMPFILE_PREFIX)
        (dump_date, dump_key) = (None, None)
        for key in key_list:
            match = pattern.match(key.key)
            if match:
                dump_date = match.group(1)
                dump_key = key
                break
        logging.warning("Downloading dump from '%s'" % dump_date)
        tempdir_name = tempfile.mkdtemp()
        if sys.platform == 'win32':
            tempfile_name = "%s\\\\%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)
        else:
            tempfile_name = "%s/%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)

        try:
            # this is a hack method, should stream this
            # all to avoid using zcat for windows
            compressed_string = dump_key.get_contents_as_string()
            compressed_stream = StringIO(compressed_string)
            gzipper = gzip.GzipFile(fileobj=compressed_stream, mode='rb')
            out_file = file(tempfile_name, mode='wb')
            for line in gzipper:
                out_file.write(line)
            out_file.close()
            gzipper.close()
            compressed_stream.close()
            host_flag = ''
            if settings.DATABASES['default']['HOST']:
                host_flag = "-h %s" % settings.DATABASES['default']['HOST']
            run_command("mysql %s -u %s -p%s %s < %s" %
                        (
                            host_flag,
                            settings.DATABASES['default']['USER'],
                            settings.DATABASES['default']['PASSWORD'],
                            settings.DATABASES['default']['NAME'],
                            tempfile_name,
                            ))
            logging.warning("Dump from '%s' restored." % dump_date)
            management.call_command('syncdb')
            if not options.get('restore_only'):
                management.call_command('migrate')
        except Exception, e:
            logging.error(e)

        # always delete command
        run_command('rm -f %s' % tempfile_name)
        run_command('rmdir %s' % tempdir_name)

from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError
from datetime import datetime
import logging
import mimetypes
import os
import tempfile

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings
from django.core.management.base import BaseCommand

from utility.run import *
from utility.backup import _BACKUP_DUMPFILE_PREFIX, _BACKUP_S3_PREFIX

class Command(BaseCommand):
    def handle(self, *args, **options):
        datestring = datetime.now().strftime("%Y%m%d%H%M%S")
        dumpfile_name = "%s%s.gz" % (_BACKUP_DUMPFILE_PREFIX, datestring)
        tempdir_name = tempfile.mkdtemp()
        tempfile_name = "%s/%s" % (tempdir_name, dumpfile_name)

        try:
            print "CREATING COMMAND"
            command = "mysqldump --opt --order-by-primary --compress --user=%s --password=%s --host=%s %s | gzip > %s" % (\
                      settings.DATABASES['default']['USER'],\
                      settings.DATABASES['default']['PASSWORD'], \
                      settings.DATABASES['default']['HOST'], \
                      settings.DATABASES['default']['NAME'], \
                      tempfile_name)
            print command
            run_command(command)

            content_type = mimetypes.guess_type(tempfile_name)[0]
            if not content_type:
                content_type = 'application/x-gzip'

            headers = {}
            connection = S3Connection(settings.AWS_ACCESS_KEY_ID,
                                      settings.AWS_SECRET_ACCESS_KEY)
            bucket = connection.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

            machine_prefix = ''
            machine_name_parser = SafeConfigParser()
            machine_name_parser.read('/etc/machine_name.ini')

            try:
                machine_prefix = '%s/' % machine_name_parser.get('machine', 'name')
            except (NoSectionError, NoOptionError):
                pass
            k = Key(bucket, "%s/%s%s" % (_BACKUP_S3_PREFIX,
                                         machine_prefix,
                                         dumpfile_name))
            headers['Content-Type'] = content_type
            headers['x-amz-acl'] = 'private'
            k.set_contents_from_filename(tempfile_name, headers=headers)
        except Exception, e:
            logging.error(e)

        # always delete command
        run_command('rm -f %s' % tempfile_name)
        run_command('rmdir %s' % tempdir_name)



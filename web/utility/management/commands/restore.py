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

from ftplib import FTP, error_perm

class Command(BaseCommand):
  option_list = BaseCommand.option_list + (
    make_option('--restore-only',
          action="store_true",
          dest="restore_only",
          default=False),
    )

  def handle(self, *args, **options):

    ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)

    candidate_list = []
    try:
      candidate_list = ftp.nlst("concierge.mysqldump*")
    except error_perm, resp:
      if str(resp) == "550 No files found":
        print "no files in directory"
      else:
        raise
    print(candidate_list)

    candidate_list = sorted(candidate_list)
    print('%d candidate dumps found' % len(candidate_list))
    print('going with: ' + str(candidate_list[0]))
    dumpfile_name = candidate_list[0]
    tempdir_name = tempfile.mkdtemp()
    if sys.platform == 'win32':
      tempfile_name = "%s\\\\%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)
    else:
      tempfile_name = "%s/%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)

    ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.retrbinary('RETR ' + dumpfile_name, open(tempfile_name, 'wb'))
    # this is a hack method, should stream this
    # all to avoid using zcat for windows
    # gzipper = gzip.GzipFile(fileobj=tempfile_name, mode='rb')
    # out_file = file(tempfile__name, mode='wb')
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
    print("Dump from '%s' restored." % dump_date)
    management.call_command('syncdb')
    if not options.get('restore_only'):
      management.call_command('migrate')

    # always delete command
    run_command('rm -f %s' % tempfile_name)
    run_command('rmdir %s' % tempdir_name)

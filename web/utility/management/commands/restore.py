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

    candidate_list.sort()
    print(candidate_list)
    print('%d candidate dumps found' % len(candidate_list))
    print('going with: ' + str(candidate_list[-1]))
    dumpfile_name = candidate_list[-1]
    tempdir_name = tempfile.mkdtemp()
    if sys.platform == 'win32':
      tempfile_name = "%s\\\\%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)
    else:
      tempfile_name = "%s/%ssql" % (tempdir_name, _BACKUP_DUMPFILE_PREFIX)


    with open(dumpfile_name, 'wb') as f:
      def writeFile (data):
        f.write(data)

      ftp = FTP(FTP_HOST, FTP_USER, FTP_PASS)
      ftp.retrbinary('RETR ' + dumpfile_name, writeFile)
      f.close()
    print("unzipping: " + dumpfile_name)
    with gzip.open(dumpfile_name, 'rb') as f:
    # this is a hack method, should stream this
    # all to avoid using zcat for windows
      file_content = f.read()
      f.close()

      out_file = open(tempfile_name, 'wb')
      out_file.writelines(file_content)
      out_file.close()
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
    print("Dump restored.")
    management.call_command('syncdb')
    if not options.get('restore_only'):
      management.call_command('migrate')

    # always delete command
    run_command('rm -f %s' % tempfile_name)
    run_command('rmdir %s' % tempdir_name)

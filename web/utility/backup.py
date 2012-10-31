from django.conf import settings

_BACKUP_DUMPFILE_PREFIX = "%s.mysqldump." % settings.DATABASES['default']['NAME']

FTP_HOST = "ftp.concierge.pewpewlasers.com"
FTP_USER = "conciergebackup"
FTP_PASS = "DR#5FVqV"

#!c:\users\andrew\documents\github\portfex\portfexenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipdb==0.13.2','console_scripts','ipdb3'
__requires__ = 'ipdb==0.13.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ipdb==0.13.2', 'console_scripts', 'ipdb3')()
    )

#!C:\Users\weibi\PycharmProjects\cse442\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==3.6','console_scripts','coverage3'
__requires__ = 'coverage==3.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coverage==3.6', 'console_scripts', 'coverage3')()
    )

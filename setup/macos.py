import os
import stat
import shutil

shutil.copy(os.getcwd()+'/src/main.py','/usr/local/bin/fir')
os.chmod('/usr/local/bin/fir', stat.S_IEXEC)
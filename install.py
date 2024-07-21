import subprocess
import shutil
import os
import stat, sys

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"

# background color
BLACKB  = "\033[40m"
REDB    = "\033[41m"
GREENB  = "\033[42m"
YELLOWB = "\033[43m"
BLUEB   = "\033[44m"
PURPLEB = "\033[45m"
CYANB   = "\033[46m"
WHITEB  = "\033[47m"

# bold
B    = "\033[1m"
BOFF = "\033[22m"

# italics
I = "\033[3m"
IOFF = "\033[23m"

# underline
U = "\033[4m"
UOFF = "\033[24m"


# reset
R  = "\033[0m"

cwd = os.getcwd()
INSTALLATION_BIN = "/usr/local/bin"
L_INSTALLATION_BIN = os.environ["HOME"]+"/.local/syndex"
L_LIB = os.environ["HOME"]+"/.local/syndex/lib"


LIBRARY_P = "/usr/local/lib"
LOCAL_INS = False

def chksu():
    if os.geteuid() != 0:
        print(YELLOW+"WARNING"+R+": You are not running this as superuser. Installation focused on local environment (not all users)")
        print("Are you sure to continue? [y/n] ", end='')
        while True:
            if input(":").lower().strip() == "y":
                LOCAL_INS = True
                return True
            else:
                exit(2)
    else: return True
            
def check_benchutils():
    global BINA_P
    if shutil.which("pip3") == None and shutil.which("pip3") == None:
        print(RED+"ERROR"+R+": Please install "+B+U+"python3-pip (PIP)"+BOFF+UOFF+" first.")
        exit(2)
    if not os.path.exists(cwd+"/"+"requirements.txt"):
        print(RED+"ERROR"+R+": Please generate your own "+B+U+"requirements.txt"+BOFF+UOFF+" \nusing "+B+U+GREEN+"python3 -m pipreqs.pipreqs"+R+" or "+B+U+GREEN+"You can download it yourself at my GitHub"+R)
        exit(2)
    BINA_P = os.environ["PATH"]
    print(BINA_P)
    
def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.remove(originalfile)
    os.rename('newfile.txt',originalfile)
    
def loc_install():
    insert("syncube.py","#!/usr/bin/env python\nimport sys\nsys.path.append(\""+L_LIB+"/\")\n")
    os.makedirs(L_INSTALLATION_BIN, exist_ok=True)
    os.makedirs(L_LIB, exist_ok=True)
    shutil.copy2(cwd+"/syncube.py", L_INSTALLATION_BIN+"/syncube")
    shutil.copy2(cwd+"/SyndexCube.py", L_LIB+"/")
    mode = os.stat(L_INSTALLATION_BIN+"/syncube").st_mode
    mode |= (mode & 0o444) >> 2 
    os.chmod(L_INSTALLATION_BIN+"/syncube", mode)
    
    
    
loc_install()
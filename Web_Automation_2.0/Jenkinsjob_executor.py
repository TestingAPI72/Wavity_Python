import re
import subprocess
import sys
from subprocess import Popen, PIPE
import os
import random


def job_executor():

    def random_string():
        return 'Exec_shell' + str(random.randint(999, 99999))

    FOLDER_PATH = '/var/lib/jenkins/workspace/Web_Automation/Web_Automation_2.0/' + random_string()
    try:
        if os.path.exists(FOLDER_PATH + '/' + 'python_executor.sh'):
            print("Folder Exists")
            os.remove(FOLDER_PATH)
        else:
            print("File doesn't exists")
    except (FileNotFoundError, FileExistsError):
        print(sys.exc_info())

    os.mkdir(FOLDER_PATH)
    p1 = subprocess.Popen(['cp', '/home/alethea/python_executor.sh', '{}'.format(FOLDER_PATH)], stdout=PIPE,
                          stderr=PIPE,
                          text=True)
    stdout, stderr = p1.communicate()
    if os.path.exists(FOLDER_PATH + '/' + 'python_executor.sh'):
        print("File Exists")
        os.chdir(FOLDER_PATH)
        p1 = subprocess.Popen(['./python_executor.sh', 'Sanity'], stderr=PIPE, stdout=PIPE, text=True)
        stdout, stderr = p1.communicate()
        print(stdout, stderr, end='\n')
    else:
        print("File doesn't exists")
        # p2 = subprocess.Popen(['rm', '-rf', '{}'.format(FOLDER_PATH)], stdout=PIPE, stderr=PIPE, text=True)
        # stdout, stderr = p2.communicate()
    if re.search('(Exec.*)', FOLDER_PATH):
        return re.search('(Exec.*)', FOLDER_PATH).group()

job_executor()

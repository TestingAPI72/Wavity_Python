import os
import pdb
import re
import subprocess
from subprocess import Popen, PIPE
import pytest


def retry_decorators(func):
    pdb.set_trace()

    def inner1():
        print("retry function Started")
        status= False
        count = 0
        while False == status:
            status = func()
            count += 1
            if count >= 10:
                break
            continue
        return inner1
    return func


@retry_decorators
def shell_file_delete():
    pdb.set_trace()
    try:
        FOLDER_PATH = '/var/lib/jenkins/workspace/Web_Automation/Web_Automation_2.0/'
        os.chdir(FOLDER_PATH)
        p1 = subprocess.Popen(['ls'], stdout=PIPE, stderr=PIPE, text=True)
        stdout, stderr = p1.communicate()
        print(stdout)
        for _ in str(stdout).splitlines():
            if re.search('(^Exec_shell\d+)', _):
                print("Folder founded")
                folder = [x.group() for x in re.finditer('(^Exec_shell\d+)', _)]
                print(folder)
                remove_folder = subprocess.Popen(['rm', '-rf', '{}'.format(folder[0])], stdout=PIPE, stderr=PIPE,
                                                 text=True)
                stdout, stderr = remove_folder.communicate()
                print(stdout)
            else:
                print("Folder Doesn't exists")
        for _ in str(stdout).splitlines():
            if not re.search('(^Exec_shell\d+)', _):
                return True
            return False
    except IndexError as e:
        print(e)


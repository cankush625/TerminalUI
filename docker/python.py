import subprocess as sp

def confPython():
    sp.run(f"sudo docker run centos /bin/bash -c 'dnf install python3 -y; echo \"print('hello')\" > aa.py; python3 aa.py'",shell=True)

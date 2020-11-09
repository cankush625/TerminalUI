import subprocess as sp

def confHttpd(imageName):
    sp.run(f"sudo docker run {imageName} /bin/bash -c 'dnf install httpd -y; /usr/sbin/httpd'", shell=True)

def confRemoteHttpd(imageName, userName, remoteIP):
    sp.run(f"ssh {userName}@{remoteIP} sudo docker run {imageName} /bin/bash -c 'dnf install httpd -y; /usr/sbin/httpd'", shell=True)
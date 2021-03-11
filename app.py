import os
import getpass
from time import sleep

from printHead.printHead import header
from linuxAutomation.configure_linux import configureLinux
from docker.webserver import confHttpd, confRemoteHttpd
from docker.python import confPython
from hadoopCluster.hadoop import configure
from kubernetesCluster.kubernetes_cluster import configure_kube_master_node
from aws.ec2_instance import launchInstance
from aws.ebs import createEbsVolume, attachEbsVolume
from aws.s3 import uploadFileToBucket
from aws.cloudfront import createDistribution

header()

# Adding password feature to authenticate the user
passwd = getpass.getpass("ENTER ADMIN PASSWORD : ")
passwd_ = 'autopy'

while passwd != passwd_:
    if passwd != passwd_:
       passwd = getpass.getpass(" WRONG PASSWORD!! TRY AGAIN : ")

os.system("tput setaf 4")
print('''
        1. Local
        2. Remote
        ''')
os.system("tput setaf 7")
location = int(input("Where do you want to run the command: "))

if location == 2:
    userName = input("Enter the remote system user name: ")
    remoteIP = input("Enter the IP address of remote system: ")

while True:
    header()
    os.system("tput setaf 4")
    print('''
            1. CONFIGURE LINUX
            2. CONFIGURE WEBSERVER IN DOCKER CONTAINER
            3. CONFIGURE PYTHON IN DOCKER CONTAINER
            4. CONFIGURE HADOOP CLUSTER
            5. CONFIGURE KUBERNETES CLUSTER
            6. HIGH AVAILABILITY ARCHITECTURE ON AWS
            7. Exit
            ''')
    os.system("tput setaf 7")

    # Taking user choice to run the command
    choice = int(input("Enter your choice(number): "))

    # Output is displayed in green color
    if choice == 1:
        header()
        configureLinux()
    elif choice == 2:
        header()
        if location == 1:
            confHttpd('centos')
        elif location == 2:
            confRemoteHttpd('centos', userName, remoteIP)
    elif choice == 3:
        header()
        confPython()
    elif choice == 4:
        header()
        configure()
    elif choice == 5:
        header()
        configure_kube_cluster()
    elif choice == 6:
        header()
        launchInstance()
        print("EC2 instance is being created...")
        sleep(60)
        createEbsVolume()
        print("EBS Volume is being created...")
        sleep(5)
        attachEbsVolume()
        uploadFileToBucket()
        print("File is being uploaded...")
        sleep(5)
        createDistribution()
    elif choice == 7:
        exit()

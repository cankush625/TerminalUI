import os
import getpass
from time import sleep

from printHead.printHead import header
from docker.webserver import confHttpd
from docker.python import confPython
from hadoopCluster.hadoop import configure
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

while True:
    header()
    os.system("tput setaf 4")
    print('''
            1. CONFIGURE WEBSERVER IN DOCKER CONTAINER
            2. CONFIGURE PYTHON IN DOCKER CONTAINER
            3. CONFIGURE HADOOP CLUSTER
            4. HIGH AVAILABILITY ARCHITECTURE ON AWS
            5. Exit
            ''')
    os.system("tput setaf 7")

    # Taking user choice to run the command
    choice = int(input("Enter your choice(number): "))

    # Output is displayed in green color
    if choice == 1:
        header()
        confHttpd('centos')
    elif choice == 2:
        header()
        confPython()
    elif choice == 3:
        header()
        configure()
    elif choice == 4:
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
    elif choice == 5:
        exit()



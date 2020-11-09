import subprocess as sp
from time import sleep

def createEbsVolume():
    availabilityZone = input("Enter the name of the availability zone: ")
    volumeType = input("Enter the volume type: ")
    size = input("Enter the volume size in GB: ")
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    command = "aws ec2 create-volume --availability-zone " + availabilityZone + " --volume-type " + volumeType + " --size " + size + " --tag-specifications ResourceType=volume,Tags=[{Key=" + key + ",Value=" + value + "}]"
    sp.run(command, shell=True)

def attachEbsVolume():
    volumeID = input("Enter the volume ID which you want to attach: ")
    instanceID = input("Enter the instance ID to which you want to attach volume: ")
    deviceName = input("Enter the device name( for example, /dev/sdh or xvdh ): ")
    sp.run("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(volumeID, instanceID, deviceName), shell=True)
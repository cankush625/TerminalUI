import subprocess as sp

def launchInstance():
    image_id = input("Enter the image(AMI) ID: ")
    instance_type = input("Enter the instance type: ")
    count = input("How many instances you want to launch?: ")
    subnet_id = input("Enter the subnet ID: ")
    security_group_id = input("Enter the security group ID: ")
    key_name = input("Enter the key name: ")

    sp.run("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5} --user-data file://aws/ud.txt".format(image_id, instance_type, count, subnet_id, security_group_id, key_name), shell=True)
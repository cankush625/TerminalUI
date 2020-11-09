import subprocess as sp

def uploadFileToBucket():
    localFileLocation = input("Enter the local file location: ")
    s3BucketLocation = input("Enter the S3 bucket location: ")
    acl = input("Enter the ACL for this file(for eg. public-read): ")
    sp.run("aws s3 cp {0} {1} --acl {2}".format(localFileLocation, s3BucketLocation, acl), shell=True)
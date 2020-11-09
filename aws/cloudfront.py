import subprocess as sp

def createDistribution():
    bucketName = input("Enter the S3 bucket name: ")
    defaultRootObject = input("Enter the name of the default root object(along with extension): ")
    sp.run("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com --default-root-object {1}".format(bucketName, defaultRootObject), shell=True)
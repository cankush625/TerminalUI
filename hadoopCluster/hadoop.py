from jinja2 import Environment, FileSystemLoader
import subprocess

def installtionScript(nodeType,directoryPath):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('installationScript.sh.j2')
    output = template.render(nodeType = nodeType , directoryPath = directoryPath)
    file = open("./temp/installationScript.sh", "w")
    file.write("%s" %(output))
    file.close()

def hdfsSite(nodeType,directoryPath):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('hdfs-site.xml.j2')
    output = template.render(nodeType = nodeType , directoryPath = directoryPath)
    file = open("./temp/hdfs-site.xml", "w")
    file.write("%s" %(output))
    file.close()

def coreSite(nodeIp,nodePort):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('core-site.xml.j2')
    output = template.render(IP = nodeIp , port = nodePort)
    file = open("./temp/core-site.xml", "w")
    file.write("%s" %(output))
    file.close()

def copyTemplate(nodeIP):
    subprocess.run(f'scp ./temp/hdfs-site.xml root@{nodeIP}:/root/hdfs-site.xml',shell=True)
    subprocess.run(f'scp ./temp/core-site.xml root@{nodeIP}:/root/core-site.xml',shell=True)

def nameNode(nameNodeIP):
    nameNodeDirectory = input('Enter Name Node Directory Name : ')
    nameNodePort = input('Enter Name Node port : ')
    hdfsSite('name',f'/root/{nameNodeDirectory}')
    coreSite(nameNodeIP,nameNodePort)
    copyTemplate(nameNodeIP)
    installtionScript('name',nameNodeDirectory)
    subprocess.run(f"ssh root@{nameNodeIP} 'bash -s' < ./temp/installationScript.sh",shell=True)
    return nameNodePort

def dataNode(dataNodeIP,nameNodeIP,nameNodePort):
    dataNodeDirectory = input('Enter Data Node Directory Name : ')
    hdfsSite('data',f'/root/{dataNodeDirectory}')
    coreSite(nameNodeIP,nameNodePort)
    copyTemplate(dataNodeIP)
    installtionScript('data',dataNodeDirectory)
    subprocess.run(f"ssh root@{dataNodeIP} 'bash -s' < ./temp/installationScript.sh",shell=True)

def configure():
    nameNodeIP = input('Enter Name Node IP : ')
    dataNodeIP = input('Enter Data Node IP : ')
    nameNodePort = nameNode(nameNodeIP)
    dataNode(dataNodeIP,nameNodeIP,nameNodePort)

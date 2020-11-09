import subprocess as sp

def webserverConf():
    sp.run("yum install httpd -y",shell=True)
    webpage = input("\tType the Webpage name(with extension): ")
    content = input("\tENTER THE CONTENT")
    saveFile = open(webpage, 'w')
    saveFile.write(content)
    saveFile.close()
    op2 = sp.getoutput("mv {} /var/www/html/".format(webpage))
    sp.run("systemctl start httpd",shell=True)
    sp.run("systemctl enable httpd",shell=True)
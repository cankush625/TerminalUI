import os
import subprocess as sp
def AnsibleAutomation():
    print("User where would you like to configure ansible?[remote/local]")
    exe = input(" Enter your choice : ")
    if exe == "local":
        local1 = os.system("yum install python3 -y")
        local2 = os.system("pip3 install ansible")
        local3 = os.system("ansible --version")
        invent = input("Enter what would be the name of your inventory? :")
        with open('ansible.cfg', 'r') as f:
            s = f.read().replace('inventory=','inventory=/new_invent/')
        with open('ansible.cfg', 'w') as f:
            f.write(s)
        local5 = os.system("mv ansible.cfg /etc/ansible/ansible.cfg")
        print("which hosts would you like to put in your inventory?")
        choice = 'Y'
        while choice == 'Y':
            lst = list()
            line = input("Enter first IP and then username and password separated by space : ")
            for each in line.split():
               # print(each)
                lst.append(each)
            if len(lst) == 1:
                ip = lst[0]
                # Open a file with access mode 'a'
                file_object = open('/new_invent/{}'.format(invent), 'a')
                # Append 'hosts ip' at the end of file
                file_object.write('{}\n'.format(ip))
                # Close the file
                file_object.close()
            elif len(lst) == 3:
                ip = lst[0]
                user = lst[1]
                passwd = lst[2]
                file_object = open('{}'.format(invent),'a')
                file_object.write('{} ansible_user={} ansible_password={}\n'.format(ip,user,passwd))
            choice = input("Would You like to continue adding hosts?[Y/N] ")
    elif exe == "remote":
        print("Select any of these available IP's:  192.168.43.22   192.168.43.30")
        ip = input("Enter IP: ")
        remote3 = sp.getoutput("ssh root@{} yum install python3 -y".format(ip))
        print(remote3)
        remote4 = sp.getoutput("ssh root@{} pip3 install ansible".format(ip))
        print(remote4)
        remote5 = sp.getoutput("ssh root@{} ansible --version".format(ip))
        print(remote5)
        inventory = input("Enter what would be the name of your inventory? :")
        with open('ansible-remote.cfg','r') as f:
            s = f.read().replace('inventory=','inventory=/new_invent/{}'.format(inventory))
        with open('ansible-remote.cfg','w') as f:
            f.write(s)
        remote6 = sp.getoutput("scp ansible-remote.cfg root@{}:/root/".format(ip))
        print(remote6)
        neww = sp.getoutput("ssh root@{} mv /root/ansible-remote.cfg /etc/ansible/ansible.cfg".format(ip))
        print(neww)
        choice = 'Y'
        while choice == 'Y':
            lst2 = list()
            line2 = input("Enter first IP and then username and password separated by space : ")
            for i in line2.split():
                lst2.append(i)
            if len(lst2) == 1:
                rem_ip=lst2[0]
                file_object = open('{}'.format(inventory), 'a')
                file_object.write('{}\n'.format(rem_ip))
                file_object.close()
            elif len(lst2) == 3:
                rem_ip = lst2[0]
                user = lst2[1]
                passwd = lst2[2]
                file_object = open('{}'.format(inventory),'a')
                file_object.write('{} ansible_user={} ansible_password={}\n'.format(rem_ip,user,passwd))
            mkdir = sp.getoutput("ssh root@{} mkdir /new_invent/".format(ip))
            move = sp.getoutput("scp {} root@{}:/new_invent/".format(inventory,ip))
            choice = input("Would You like to continue adding hosts?[Y/N] ")
AnsibleAutomation()

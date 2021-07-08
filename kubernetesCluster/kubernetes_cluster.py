import subprocess as sp
from jinja2 import Environment, FileSystemLoader
import time

from printHead.printHead import header

def configure_kube_cluster():
    while True:
        header()
        sp.run("tput setaf 4", shell=True)
        print('''
                1. CONFIGURE KUBERNETES MASTER NODE
                2. CONFIGURE KUBERNETES SLAVE NODE
                3. Exit
                ''')
        sp.run("tput setaf 7", shell=True)

        # Taking user choice to run the command
        choice = int(input("Enter your choice(number): "))

        # Output is displayed in green color
        if choice == 1:
            header()
            configure_kube_master_node()
        elif choice == 2:
            header()
            configure_kube_slave_node()
        elif choice == 3:
            exit()

def configure_kube_master_playbook(pod_network_cidr, owner, group):
    file_loader = FileSystemLoader('kubernetesCluster/templates')
    env = Environment(loader = file_loader)
    template = env.get_template('kube_master.yml.j2')
    output = template.render(pod_network_cidr = pod_network_cidr , owner = owner, group = group)
    file = open("./kubernetesCluster/temp/kube_master.yml", "w")
    file.write("%s" %(output))
    file.close()

def configure_kube_master_node():
    pod_network_cidr = input("Enter the pod network cidr: ")
    owner = input("Enter the owner: ")
    group = input("Enter the group: ")
    configure_kube_master_playbook(pod_network_cidr, owner, group)
    sp.run("ansible-playbook ./kubernetesCluster/temp/kube_master.yml", shell=True)

def configure_kube_slave_playbook(kube_join_command):
    file_loader = FileSystemLoader('kubernetesCluster/templates')
    env = Environment(loader = file_loader)
    template = env.get_template('kube_slave.yml.j2')
    output = template.render(kube_join_command = kube_join_command)
    file = open("./kubernetesCluster/temp/kube_slave.yml", "w")
    file.write("%s" %(output))
    file.close()

def configure_kube_slave_node():
    kube_join_command = input("Enter the kube join command: ")
    configure_kube_slave_playbook(kube_join_command)
    sp.run("ansible-playbook ./kubernetesCluster/temp/kube_slave.yml", shell=True)
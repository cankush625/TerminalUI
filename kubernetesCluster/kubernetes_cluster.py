import subprocess as sp
from jinja2 import Environment, FileSystemLoader
import time

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
    time.sleep(500)
import subprocess as sp

def runCommands():
    command = input("Enter the command: ")
    sp.run("{0}".format(command),shell=True)
    input("Enter to continue...")
import subprocess as sp

from printHead.printHead import header
from linuxAutomation.linux_commands import runCommands
from linuxAutomation.webserver import webserverConf
from linuxAutomation.docker import installDocker, startDocker, dockerCommands

def configureLinux():
    while True:
        header()
        sp.run("tput setaf 4", shell=True)
        print('''
                1. RUN LINUX COMMANDS
                2. CONFIGURE WEBSERVER
                3. INSTALL DOCKER
                4. DOCKER COMMANDS
                5. Exit
                ''')
        sp.run("tput setaf 7", shell=True)

        # Taking user choice to run the command
        choice = int(input("Enter your choice(number): "))

        # Output is displayed in green color
        if choice == 1:
            header()
            runCommands()
        elif choice == 2:
            header()
            webserverConf()
        elif choice == 3:
            header()
            installDocker()
            startDocker()
        elif choice == 4:
            header()
            dockerCommands()
        elif choice == 5:
            exit()
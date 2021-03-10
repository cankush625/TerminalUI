import subprocess as sp

def installDocker():
    sp.run("yum install docker-ce --nobest -y", shell=True)

def startDocker():
    sp.run("systemctl start docker",shell=True)

def dockerCommands():
    ch = 'Y'
    cnt = 0
    while ch =='Y':
        if cnt == 0:
            ans = input("would you like to play with containers?[Y/N]")
        if ans == 'Y':
            print("CHOOSE OPERATION: ")
            print(" 1 : RUN ")
            print(" 2 : STOP")
            print(" 3 : REMOVE CONTAINER")
            print(" 4 : REMOVE IMAGE")
            print(" 5 : PULL IMAGE")
            print(" 6 : Exit")
            opt = int(input())
            if opt == 1:
                name = input("GIVE NAME TO YOUR CONTIANER: ")
                term = input("WOULD YOU LIKE TO GET INTERACTIVE TERMINAL OR CLOSE CONT AFTER RUNNING?[Y/N]")
                image = input("IMAGE NAME : ")
                cont_run = sp.getoutput("docker run -dit --name {} {}".format(name, image))
                print(cont_run)
                op_of_cont = sp.getoutput("docker ps")
                print(op_of_cont)
            elif opt == 2:
                all_cont = sp.getoutput("docker ps")
                print("LIST OF CONTAINERS RUNNING")
                print(all_cont)
                cont_name = input("ENTER THE NAME OF CONTAINER TO BE STOPPED: ")
                cont_stop = sp.getoutput("docker stop {}".format(cont_name))
                print(cont_stop)
                clear = sp.run("clear",shell=True)
                check_stop_cont = sp.getoutput("docker ps")
                print(check_stop_cont)
            elif opt == 3:
                all_cont = sp.getoutput("docker ps -a")
                print(all_cont)
                rm_cont_name = input("IF ALL WANT TO REMOVE TYPE all or ENTER THE NAME OF CONTAINER TO BE REMOVED: ")
                if rm_cont_name == "all":
                    rm_cont = sp.getoutput("docker rm `docker ps -a`")
                else:
                    rm_cont = sp.getoutput("docker rm {}".format(rm_cont_name))
                print(rm_cont)
                check_rm_cont = sp.getoutput("docker ps -a")
                print(check_rm_cont)
            elif opt == 4:
                all_img = sp.getoutput("docker images")
                print(all_img)
                rm_img_name = input("IF ALL WANT TO REMOVE TYPE all OR ENTER NAME OF IMAGE TO BE DELETED: ")
                if rm_img_name == "all":
                    rm_img = sp.getoutput("docker rmi `docker images -q` --force")
                else:
                    rm_img = sp.getoutput("docker rmi {}".format(rm_img_name))
                print(rm_img)
                check_rm_img = sp.getoutput("docker images")
                print(check_rm_img)
            elif opt == 5:
                all_img_present = sp.getoutput("docker images")
                print("LIST OF ALL CONTAINERS PRESENT")
                print(all_img_present)
                pull_img_name = input("ENTER NAME OF IMAGE TO BE PULLED: ")
                pull_img = sp.getoutput("docker pull {}".format(pull_img_name))
                print(pull_img)
                check_pull_img = sp.getoutput("docker images")
                print(check_pull_img)
            elif opt == 6:
                break;
            ch = input("WOULD YOU LIKE TO CONTINUE?[Y/N]: ")
            if ch != 'Y':
                break
            cnt+=1
        else:
            break
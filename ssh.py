
# ------------------------------ Library Imports ----------------------------- #

import os
from time import sleep


# ----------------------------- Global Variables ----------------------------- #

filePath = "conf.txt"
file = ""

serverName = ""
serverIP = ""
serverUser = ""
serverPass = ""



# ------------------------------ Main Definition ----------------------------- #
def main():
    global file, serverName, serverIP, serverUser, serverPass
    
    file = open(filePath).readlines()
    serverName = file[0].split()[1]
    serverIP = file[1].split()[1]
    serverUser = file[2].split()[1]
    serverPass = file[3].split()[1]

    start_user()
    
    while True:
        sleep(1)


# -------------------------------- Hidden SSH -------------------------------- #
def start_hidden():
    print("\n Starting Hidden SSH Session...")


# --------------------------------- User SSH --------------------------------- #
def start_user():
    global user, ip
    
    print("\n Starting Hidden SSH Session...")
    print("	- Logging in as " + serverUser + " at " + serverName + " (" + serverIP + ")")
    os.system("sshpass " + "-f " + "pass.txt " + serverUser + "@" + serverIP)
    
    
    



# --------------------------------- Call Main -------------------------------- #
main()
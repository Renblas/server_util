
# ------------------------------ Library Imports ----------------------------- #

import os
from time import sleep


# ----------------------------- Global Variables ----------------------------- #

filePath = "conf.txt"
file = ""

serverName = ""
serverIP = ""
serverUser = ""



# ------------------------------ Main Definition ----------------------------- #
def main():
    global file, serverName, serverIP, serverUser
    
    file = open(filePath).readlines()
    serverName = file[0].split()[1]
    serverIP = file[1].split()[1]
    serverUser = file[2].split()[1]

    start_user()
    
    while True:
        sleep(1)


# -------------------------------- Hidden SSH -------------------------------- #
def start_hidden():
    print("\n Starting Hidden SSH Session...")


# --------------------------------- User SSH --------------------------------- #
def start_user():
    global user, ip
    
    print("\n Starting User SSH Session...")
    print("	- Logging in as " + serverUser + " at " + serverName + " (" + serverIP + ") \n\n")
    os.system("ssh " + serverUser + "@" + serverIP)
    
    
    



# --------------------------------- Call Main -------------------------------- #
main()
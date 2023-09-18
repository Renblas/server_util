
# --------------------------- All Libs And Imports --------------------------- #

import os
import signal
import subprocess

import math

from time import sleep

import gi.repository
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository import AppIndicator3

from tkinter import *
from tkinter import ttk as tk


# ------------------------------- Create Tk Gui ------------------------------ #
app = None
menu = None

# --------------------------------- Constants -------------------------------- #
APPINDICATOR_ID = "server_util"
iconpath =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon3.png")

serverName = "HomeServer"

vpnActive = False
   

# ============================================================================ #
#                                 Main Function                                #
# ============================================================================ #
def main():
    
    global app, Gtk, vpnActive
    
    # Setup
    os.setpgrp()
    
    if get_vpn_status():
        vpnActive = True
    
    init_top_bar()
    
    # update top bar / gui events
    while True:
        
        if (app):
            app.update_idletasks()
            app.update()
            
            app.update_internal()
            
        Gtk.main_iteration_do(False)
        
        sleep(1/10)
  

# ============================================================================ #
#                           Application Window Class                           #
# ============================================================================ #
class Application(tk.Frame): 
    # init da shit             
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()
        
    # update things like text etc based on vpn status
    def update_internal(self):
        
        global vpnActive
        
        vpnActive = get_vpn_status()
        # ["interface", "handshake", "transfer", "recieved"]
            
        # if has connection to VPN
        if vpnActive:
            self.sshButton.config(text="Deactivate VPN")
        
        # if no current connection to VPN
        else:
            self.sshButton.config(text="Activate VPN")

	# Create Elements inside App Window
    def createWidgets(self):
        
        # Quit Button
        self.quitButton = tk.Button(self, text='Quit', command=self.sudoku)            
        self.quitButton.grid() 
        
        # Activate/deactivate ssh
        self.sshButton = tk.Button(self, text='Activate SSH', command=self.activateSSH)
        self.sshButton.grid()
    
    
    def sudoku(self):    
        print("\n Et tu Brutus...")    
        os.killpg(os.getpgid(os.getpid()), signal.SIGKILL)
    
    # Activate/Deactivate VPN based on current wg show status
    def activateSSH(self):
        if vpnActive:
            print("\n Deactivating VPN...")
            string = get_cmd_output("sudo wg-quick down " + serverName, [])
            
        else:
            print("\n Activating VPN...")
            string = get_cmd_output("sudo wg-quick up " + serverName, [])
			
            
    
    
        
        
 
# ============================================================================ #
#                               Utility Functions                              #
# ============================================================================ #
        
# --------------- Init App Window From Class, Called By Top Bar -------------- #
def init_app(str):
    print("\n Creating app window...")
    global app
    app = Application()
    
    
 
# ------------------------------ GUI Definitions ----------------------------- #
def init_top_bar():
    
    global menu, indicator, app
    print("\n Creating top bar...")
    
    menu = Gtk.Menu()
    
    option_open = Gtk.MenuItem.new_with_label('Open Server Utility')
    option_open.connect('activate', init_app)
    menu.append(option_open)

    option_quit = Gtk.MenuItem.new_with_label('Quit')
    option_quit.connect('activate', quit)
    menu.append(option_quit)
    
    menu.show_all()
    
    indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, iconpath, AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu)
 
 
 
# ------------------------- Execute Command In Shell ------------------------- #
def get_cmd_output(string, arr):
    string = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
    chunks = string.split()
    result = []
    for a in arr:
        for i, c in enumerate(chunks):
            try:
                j = c.index(a)
            except:
                continue
            
            result.append(chunks[i+1])
            
    return result
            
 
 
 
# --------------------------- Read Wireguard Status -------------------------- #
def get_vpn_status():
    a = ["interface"]
    arr = get_cmd_output("sudo wg show", a)
    if (len(arr) > 0 and arr[0] == serverName):
        return True
    else:
        return False
    
    
    
    
# -------------------------- Call Main + Other Stuff ------------------------- #
main()
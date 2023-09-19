# server_util

a simple python script server utility to manage a wireguard vpn connection to an external server

note this is a wip and not really intended for general use
if anyone does want to use this feel free to fork and use/adapt/rewrite as you wish

## Features:

- Manage Wireguard Connections with easy to use GUI
- Automatically start ssh connections to that server

I made this for Ubuntu so should work generally for linux, have no idea about windows or mac

## Dependencies

The following packages / python libs may need to be installed:
- sshpass 


## To Use:
1. Create a file called "conf.txt" that looks like the sample below
   ```
		name: <insert name of wireguard configuration>
		ip: <private ip of server (for ssh)>
		user: <user name to connect to server with>
   ```

2. Create a file called pass.text
	```
		<password goes here>
	```
		
Both files are used by the sshpass to start the ssh connection

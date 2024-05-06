                                ##################################################
                                ##												##
                                ##		Log Analyzer Project:					##
                                ##		Written by:								##
                                ##		           Mugabe Ignace				##
                                ##												##
                                ##################################################

import os
import subprocess



def main():
	
	# 1. Extract command usage.			
	#  cat /var/log/auth.log | grep -i command | awk -F ']' '{print  $1 "]"  $2 "]" $(NF-1) "]"}' | awk '{print $1 $2 $3 "   " $9 "    " $10}'
	commands = []
	with open('/var/log/auth.log', 'r') as log:
		for line in log:
			if("command" or "COMMAND") in line:
				commands.append(line.strip())	
	
	for line in commands:
		
		timeStamp = line.split()[0] + " " + line.split()[1] + " " + line.split()[2] # Include the Timestamp.
		
		users = line.split()[8]   # Include the executing user.
		
		usedcommand = line.split()[11]  # Include the command.
		
	#	print(f"{timeStamp}  {users}  {usedcommand}")
	
	
	
	# 2. Monitor user authentication changes.
	# cat /var/log/auth.log | egrep -a 'su: | sudo:' | grep -i 'command' | awk '{print $1 " " $2 " " $3 "\t" $12 "\t" $14}'
	
	# Print details of newly added users, including the Timestamp.
	# cat /var/log/auth.log | grep -a 'adduser'
	newusers=[]
	
	# Print details of deleted users, including the Timestamp.
	# cat /var/log/auth.log | grep -a 'deluser'
	delusers =[]
	
	# Print details of changing passwords, including the Timestamp.
	# cat /var/log/auth.log | grep -a 'passwd' | grep -a 'sudo'
	passch = []
	
	# Print details of users who used the sudo; include the command.
	indata = subprocess.check_output("cat /var/log/auth.log | grep -a 'sudo:' | grep -i command ", shell=True).decode("utf-8").split('\n')
	for info in indata:
		print(info.split(';')[-2:])
	
	
	# Print ALERT! If users failed to use the sudo command; include the command.
	# cat /var/log/auth.log | grep -a 'sudo' | grep 'failure'


	
	
	# Print details of when users used the su command.
	usedsu = subprocess.check_output("cat /var/log/auth.log | grep -a 'su:'", shell=True).decode("utf-8").split('\n')
	for period in usedsu:
		if period != "":
			#print(f"The user used su command on: {period[:16]}")
			print()

main()


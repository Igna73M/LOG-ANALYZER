                                ##################################################
                                ##												##
                                ##		Log Analyzer Project:					##
                                ##		Written by:								##
                                ##		           Mugabe Ignace				##
                                ##												##
                                ##################################################

import os
import sys
import time



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
	
		print(f"{timeStamp}  {users}  {usedcommand}")
	
	
	# 2. Monitor user authentication changes.
	# cat /var/log/auth.log | egrep -a 'su: | sudo:' | grep -i 'command' | awk '{print $1 " " $2 " " $3 "\t" $12 "\t" $14}'
	Monitor = []
	print()
	with open('/var/log/auth.log') as log2:
		print("User Authentication Changes: ")
	
	# 2.1. Print details of newly added users, including the Timestamp.
		if "useradd" in line:
			Monitor.append(line.strip())
	
	# 2.2. Print details of deleted users, including the Timestamp.
		elif "userdel" in line:
			Monitor.append(line.strip())
	
	# 2.3. Print details of changing passwords, including the Timestamp.
		elif "passwd" in line:
			Monitor.append(line.strip())
	
	# 2.4. Print details of when users used the su command.
		print()
	
	# 2.5. Print details of users who used the sudo; include the command.
		elif "COMMAND"
	
	# 2.6. Print ALERT! If users failed to use the sudo command; include the command.
		print()
		print(Monitor)
	
	print()

main()


                                ##################################################
                                ##												##
                                ##		Log Analyzer Project:					##
                                ##		Written by:								##
                                ##		           Mugabe Ignace				##
                                ##												##
                                ##################################################

import os
import subprocess


# Read log file
commands = []
passch = []
delusers =[]
newusers=[]

with open('/var/log/auth.log', 'r') as log:
	for line in log:
		if("command" or "COMMAND") in line:
			commands.append(line.strip())
		if("/passwd") in line:
			passch.append(line.strip())	
		if("/deluser") in line:
			delusers.append(line.strip())
		if("/adduser") in line:
			newusers.append(line.strip())
	

def commandextract():
	print()
	# Extract command usage.			
	print("=> List of details of Commands used: ")	
	print()
	for line in commands:
		
		timeStamp = line.split()[0] + " " + line.split()[1] + " " + line.split()[2] # Include the Timestamp.
		
		users = line.split()[8]   # Include the executing user.
		
		usedcommand = line.split()[11]  # Include the command.
			
		print(f"{timeStamp}  {users}  {usedcommand}")
		
def addedinfo():
	print()
	# Print details of newly added users, including the Timestamp.
	print("=> Information on New Added Users: ")
	print()
	for line in newusers:
		print(line)

def deletedinfo():
	print()
	# Print details of deleted users, including the Timestamp.
	print("Information of deleted users: ")
	for line in delusers:
		print(line)

def passchange():
	print()
	# Print details of changing passwords, including the Timestamp.
	print("=> When there was password Change: ")
	print()
	for line in passch:
		print(line)

def sudouse():
	print()
	# Print details of users who used the sudo; include the command.
	indata = subprocess.check_output("cat /var/log/auth.log | grep -a 'sudo:' | grep -i command ", shell=True).decode("utf-8").split('\n')
	print("=> When The user used sudo privilage: ")
	print()
	for info in indata:
		linecheck = info.split(';')[-2:]
		print(f"{linecheck[0]}	{linecheck[-1]}")

def sudofail():
	print()
	# Print ALERT! If users failed to use the sudo command; include the command.
	failedRoot = subprocess.check_output("cat /var/log/auth.log | grep -a 'sudo' | grep 'fail'", shell=True).decode("utf-8").split('\n')
	print("=> sudo execution fail: ")
	print()
	for fpr in failedRoot:
		print(fpr)

def sucommanduse():
	print()
	# Print details of when users used the su command.
	usedsu = subprocess.check_output("cat /var/log/auth.log | grep -a 'su:'", shell=True).decode("utf-8").split('\n')
	print("=> There was the use of su command: ")
	print()
	for period in usedsu:
		if period != "":
			print(f"The user used su command on: {period[:16]}")



def main():
	print()
	
	print("This is Log Analyzer Tool")
	
	print("make choice: ")
	print("1. Extract command usage.")
	print("2. Monitor user authentication changes.")
	
	choice = input(": ")
	
	if choice == '1':
		commandextract()
		
	elif choice == '2':
		print()
		print("make choice: ")
		print("1. Print details of newly added users, including the Timestamp.")
		print("2. Print details of deleted users, including the Timestamp.")
		print("3. Print details of changing passwords, including the Timestamp.")
		print("4. Print details of when users used the su command.")
		print("5. Print details of users who used the sudo; include the command.")
		print("6. Print ALERT! If users failed to use the sudo command; include the command.")

		choose = input(": ")
		
		if choose == '1':
			addedinfo()
		elif choose == '2':
			deletedinfo()
		elif choose == '3':
			passchange()
		elif choose == '4':
			sucommanduse()
		elif choose == '5':
			sudouse()
		elif choose == '6':
			sudofail()		
	
	print()
	

main()


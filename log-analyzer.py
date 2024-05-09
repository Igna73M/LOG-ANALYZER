                            ########################################
                            ##									  ##
                            ##		Log Analyzer Project:		  ##
                            ##		Written by:					  ##
                            ##		           Mugabe Ignace	  ##
                            ##      GitHub:                       ##
                            ##              Mugabe000             ##
                            ##									  ##
                            ########################################

import os
import sys


mplatform = sys.platform

if mplatform == 'linux' :
	
	commands = []
	passch = []
	delusers =[]
	newusers=[]
	
	# Read log file
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
		
	
	
	# Extract command usage.
	def commandextract():
		print()
					
		print("=> List of details of Commands used: ")	
		print()
		for line in commands:
			
			timeStamp = line.split()[0] + " " + line.split()[1] + " " + line.split()[2] # Include the Timestamp.
			
			users = line.split()[8]   # Include the executing user.
			
			usedcommand = line.split()[11]  # Include the command.
				
			print(f"{timeStamp}  {users}  {usedcommand}")
	
	
	# Print details of newly added users, including the Timestamp.
	def addedinfo():
		print()
		
		print("=> Information on New Added Users: ")
		print()
		for line in newusers:
			print(line)


	# Print details of deleted users, including the Timestamp.
	def deletedinfo():
		print()
		
		print("Information of deleted users: ")
		for line in delusers:
			print(line)


	# Print details of changing passwords, including the Timestamp.
	def passchange():
		print()
		
		print("=> When there was password Change: ")
		print()
		for line in passch:
			print(line)


	# Print details of users who used the sudo; include the command.
	def sudouse():
		print()
		
		# Open the auth.log file and read its content
		with open('/var/log/auth.log', 'r') as auth_log:
			log_lines = auth_log.readlines()
		
		# Filter lines containing 'sudo' and 'COMMAND' (case-insensitive)
		sudo_command_lines = [line for line in log_lines if 'sudo:' in line and 'COMMAND' in line.upper()]
		
		print("=> When The user used sudo privilege: ")
		print()
		for line in sudo_command_lines:
			line_parts = line.split(';')
			print(f"{line_parts[-2].strip()} {line_parts[-1].strip()}")


	# Print ALERT! If users failed to use the sudo command; include the command.
	def sudofail():
		print()
		
		# Open the auth.log file and read its content
		with open('/var/log/auth.log', 'r') as auth_log:
			log_lines = auth_log.readlines()
		
		# Filter lines containing 'sudo' and 'fail'
		failed_sudo_lines = [line for line in log_lines if 'sudo' in line and 'fail' in line]
		
		if failed_sudo_lines:
			print("=> ALERT! sudo execution failed: ")
			print()
			for line in failed_sudo_lines:
				print(line.strip())
		else:
			print("=> No sudo execution failures found.")


	# Print details of when users used the su command.
	def sucommanduse():
		print()
		
		# Open the auth.log file and read its content
		with open('/var/log/auth.log', 'r') as auth_log:
			log_lines = auth_log.readlines()
		
		# Filter lines containing 'su:'
		su_lines = [line for line in log_lines if 'su:' in line]
		
		print("=> There was the use of su command: ")
		print()
		for line in su_lines:
			timestamp = line.split()[0] + ' ' + line.split()[1] + ' ' + line.split()[2]
			print(f"The user used su command on: {timestamp}")




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
			else:
				main()
		else:
			main()
		
		print()
		
	
	main()
elif mplatform == 'win32':
	print("Script works on Linux systems only!")

# Project Structure
# 1. Log Parse auth.log: Extract command usage.
# 1.1. Include the Timestamp.
# 1.2. Include the executing user.
# 1.3. Include the command.
# 2. Log Parse auth.log: Monitor user authentication changes.
# 2.1. Print details of newly added users, including the Timestamp.
# 2.2. Print details of deleted users, including the Timestamp.
# 2.3. Print details of changing passwords, including the Timestamp.
# 2.4. Print details of when users used the su command.
# 2.5. Print details of users who used the sudo; include the command.
# 2.6. Print ALERT! If users failed to use the sudo command; include the command.
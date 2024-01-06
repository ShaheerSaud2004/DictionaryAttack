##CREATED BY SHAHEER SAUD 

import hashlib

# Function to hash a given text using MD5 algorithm
def md5_hash(text):
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    return md5_hash

# Read the list of common passwords from the 'rockyou.txt' file
with open("/Users/shaheersaud/Downloads/rockyou.txt", "r", encoding="latin-1") as file:
    common_passwords = file.read().splitlines()

# Prompt the user to enter a password to check
print("What password do you want to check to see if it is easy to hack?")
my_password = input("Enter password: ")
hashtext = md5_hash(my_password)
print("***USING MD5 ALGO TO CONVERT INPUT INTO HASH**")
print("***ITERATING THROUGH LIST OF COMMON PASSWORDS TO SEE IF HASH MATCHES***")

# Initialize a flag to track if a match is found
match_flag = False

# Iterate through each password in the list of common passwords
for password in common_passwords:
    if md5_hash(password) == hashtext:
        print("FOUND MATCH. CLIENT PASSWORD IS:*** " + password + "***.")
        match_flag = True
        break

# Check if a match was found
if not match_flag:
    print("NO MATCH FOUND IN 4,341,564 UNIQUE PASSWORDS, USED IN 32,603,388 ACCOUNTS. YOUR PASSWORD IS AT LEAST MINIMALLY PROTECTED AGAINST SIMPLE MD5 HASH ATTACKS USING COMMON PASSWORD DATABASES.")


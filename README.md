Password Security Check Tool
This program is a password security check tool that uses the MD5 hashing algorithm to determine if a user's password is among a list of common passwords. The tool is designed to help users understand the security level of their passwords by checking them against a known list of frequently used passwords. Additionally, it is deployed as a full-stack web application using Flask and Heroku.

Live Demo: https://password-checker-81c2ae152311.herokuapp.com/

How It Works
MD5 Hash Function
The program defines a function md5_hash which takes a string input (text), encodes it to bytes, and then generates an MD5 hash of this string. It returns the hash in hexadecimal format.

Loading Common Passwords
It reads a list of common passwords from a file named rockyou.txt. This file is expected to contain a large number of commonly used passwords, each on a new line. The file is opened with latin-1 encoding to accommodate different character encodings that might be present in the file.

User Input for Password
The program prompts the user to enter a password they want to check for its security against common password attacks. The entered password is then converted into an MD5 hash using the md5_hash function.

Checking Against Common Passwords
The program iterates over each password in the list of common passwords, hashing each one and comparing it to the hashed version of the user's input. If a match is found, it means the user's password is common and potentially vulnerable to an attack using this list. The program then prints a message indicating a match was found.

No Match Found Case
If no match is found after checking all the passwords in the list, the program prints a message stating that no match was found. This implies that the user's password is not in this particular list of common passwords, suggesting a minimum level of protection against attacks that use such common password lists.

Security Implication
The program essentially checks if the user's password is easy to guess or crack using a dictionary attack method with a known list of common passwords. It's important to note that just because a password isn't found in this list doesn't mean it's strong or secure against other types of attacks.

Full-Stack Web Application
This project is also deployed as a full-stack web application, making it accessible to users through a web browser. The application was developed using Flask for the backend and deployed on Heroku.

Features:
Frontend: HTML, CSS, and JavaScript were used to create a responsive and user-friendly interface.
Backend: Flask was used to handle HTTP requests, process the password checks, and interact with the frontend.
Deployment: The application is hosted on Heroku, ensuring it is available online for users to check their password security.

Live Demo
You can try the live version of this tool here: Password Security Check Tool

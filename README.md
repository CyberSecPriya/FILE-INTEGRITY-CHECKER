# FILE-INTEGRITY CHECKER-MONITERITING SCRIPT

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : PRIYA BABARE

*INTERN ID* : CT04DA834 

*DOMAIN* : CYBER  SECURITY & ETHICAL  HACKING

*DURATION*: 4 WEEKS

*MENTOR* : NEELA SANTOSH

# DESCRIPTION

This project is basic File Integrity Checker Tool written in Python. It builds to detect wheather file has been modified or not.

# Example

If you saved an important file like a (report, system file), and you want to make sure that nobody modify or tampers with it. This tool helps you to do that.

# Why it's useful

In Cybersecurity, it's important to know that file was changed or not especially by hackers, malware, or during unauthorized access. This script helps you detect file tampering.

# Features
 
1. Accepts any filename as input from the user.

2. Generates a SHA-256 hash of the given file (a secure and widely used hashing method).

3. Saves the original hash to a separate file called hashes.txt.

4. On rechecking, it compares the saved hash with the current file hash.

5. If hashes match, it says the file is unchanged. If not, it warns that the file has been 
   modified.

6. Prevents false results by checking if the hash file exists before comparing.

7. Clean and readable code that’s beginner-friendly.

# How it works

1. The script asks the user to enter the name of the file they want to verify.

2. It calculates the SHA-256 hash of that file using Python’s hashlib module.
 
3. If a saved hash doesn't exist, it saves the current hash.
 
4. If a hash is already saved, it compares the current hash with the saved one.
 
5. Output message shows whether the file is **unchanged** or **modified**.

 

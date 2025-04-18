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

 Generates SHA-256 hash of a given file  
 Saves the original hash in a file (`hashes.txt`)  
 Compares the current file hash with the saved one  
 Alerts you if the file is unchanged or has been modified

 # Explaination (Python Script)

 # 1. Importing Modules

   import hashlib

-> import : is a keyword

-> hashlib : A built-in Python module.

-> Purpose : Used to create hashes (like SHA-256 or MD5) which are unique digital fingerprints of file content.

   import os
   
-> os : Another built-in module.

-> Purpose : Allows us to interact with the operating system (like checking if a file exists).

# 2. Function to Generate Hash

def get_file_hash(filename):

-> def: Used to define a function.

-> get_file_hash: The name of the function.

-> filename: Parameter that takes a file name (like test.txt).



 

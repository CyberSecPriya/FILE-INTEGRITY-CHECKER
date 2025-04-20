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

 # How to Run the Script
 
1. Make sure Python is installed on your system. You can download it from python.org.

2. Save the Python script with a name like ( eg.task1.py.)

3. Create a test file (e.g., test.txt) in the same folder with some sample content.

4. Open VS Code, Terminal, or any Python environment.

5. Run the script using:
   python task1.py
   
6. Enter the filename when prompted (e.g., test.txt).

7. Observe the output – whether the file is unchanged or modified.
   
# Precautions to Take

1. Protect the hashes.txt file – Store it securely and don't allow unauthorized edits.

2. Use strong hashing algorithms – Like SHA-256 (which you are already using).

3. Verify the correct file – Always enter the right filename, not the script itself.

4. Save the hash before making any changes – So the tool can detect modifications accurately.

5. Avoid sharing sensitive files – Only share the script and sample outputs, not personal or secure data.

6. Organize files properly – Keep your script and test files in one secure folder.

# Output

**First Run** (Original File)

![Image](https://github.com/user-attachments/assets/992d5d14-010a-48e1-9747-7f7b62930343)

**Second Run** (NO Changes)

![Image](https://github.com/user-attachments/assets/46edb568-d127-401d-beff-5f2a972a2103)

**Third Run** (After Modify File task1.py)

![Image](https://github.com/user-attachments/assets/ccb0be17-f746-4284-a473-405a364d3400)

# Conclusion

This Python-based File Integrity Checker is a great starting point to understand file security and hash verification. It gives you hands-on experience with real-world cybersecurity concepts in a simple way. Whether you're a student, intern, or beginner in the field, this project introduces you to how professionals ensure data integrity and detect file tampering.
It also strengthens your Python skills while applying them in a practical cybersecurity scenario.

 

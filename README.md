# FILE-INTEGRITY CHECKER-MONITERITING SCRIPT

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : PRIYA BABARE

*INTERN ID* : CT04DA834 

*DOMAIN* : CYBER  SECURITY & ETHICAL  HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

# DESCRIPTION

This project is **basic File Integrity Checker Tool** written in Python. Its primary purpose is to detect whether a file has been modified by comparing cryptographic hash values. It provides a simple, efficient, and beginner-friendly way to monitor file changes and ensure that your data remains untouched. This tool can be especially useful in cybersecurity to detect tampering or unauthorized alterations.  

# EXAMPLE

Suppose you have saved an important document such as a **report, confidential system configuration, or legal file,** and you want to make sure that no one tampers with it later. This tool will help you verify the integrity of that file. If even a single byte is changed, the hash value changes, and the script will alert you that the file has been modified.

# WHY IT'S USEFUL

In the field of **cybersecurity**, maintaining the integrity of files is critical. Malware, hackers, or even accidental edits can change files without your awareness. This File Integrity Checker helps detect such unauthorized changes using SHA-256, one of the most secure hashing algorithms available. It adds an extra layer of protection by ensuring files are in their original, untampered state.

# FEATURES
 
- Accepts any filename as input from the user.

- Generates a SHA-256 hash of the given file (a secure and widely used hashing method).

- Saves the original hash to a separate file called `hashes.txt`.

- On rechecking, it compares the saved hash with the current file hash.

- If hashes match, it says the file is unchanged. If not, it warns that the file has been 
   modified.

- Prevents false results by checking if the hash file exists before comparing.

- Clean and readable code that’s beginner-friendly.

# HOW IT WORKS

1. The script asks the user to enter the name of the file they want to verify.

2. It calculates the SHA-256 hash of that file using Python’s `hashlib` module.
 
3. If it’s the first run, it saves the hash to `hashes.txt`.
 
4. If a hash is already saved, it compares the current hash with the saved one.
 
5. Based on the comparison, it shows whether the file is **unchanged** or has been **modified**.

 # HOW THE SCRIPT RUN
 
- Ensure Python is installed on your system. Download from python.org.

- Save the script with a name like `task1.py`.

- Create a test file (e.g., `test.txt` ) in the same folder.

- Open your VS Code, Terminal, or any Python-compatible environment.

- Run the script using:

```bash

   python task1.py
```

- Enter the test file name when prompted.

- Observe the output message – **“File Unchanged”** or **“File Modified.”**



# PRECAUTIONS TO TAKE

- Protect the `hashes.txt` file – Store it securely and don't allow unauthorized edits.

- Use strong hashing algorithms – Like SHA-256 (which you are already using).

- Verify the correct file – Always enter the right filename, not the script itself.

- Save the hash before making any changes – So the tool can detect modifications accurately.

- Avoid sharing sensitive files – Only share the script and sample outputs, not personal or secure data.

- Organize files properly – Keep your script and test files in one secure folder.

# OUTPUT

**First Run** (Original File)

![Image](https://github.com/user-attachments/assets/992d5d14-010a-48e1-9747-7f7b62930343)

**Second Run** (NO Changes)

![Image](https://github.com/user-attachments/assets/46edb568-d127-401d-beff-5f2a972a2103)

**Third Run** (After Modify File `task1.py`)

![Image](https://github.com/user-attachments/assets/ccb0be17-f746-4284-a473-405a364d3400)

# NOTE

- This tool is made for learning and basic file monitoring.

- It checks one file at a time and uses SHA-256 for strong hash checking.

- Run the script in a safe environment to get correct results.

- Make sure the file name you enter is correct and in the same folder as the script.

- You can improve this tool later by adding features like checking folders, sending alerts, or 
  logging changes.

# CONCLUSION

This Python-based **File Integrity Checker** is a great way to begin understanding the importance of **data integrity and hash-based verification**. It offers hands-on experience with real-world cybersecurity practices. Whether you're a student, intern, or a beginner, this project provides you with foundational knowledge of how professionals ensure data authenticity and guard against tampering. Additionally, it enhances your Python skills by applying them in a practical and meaningful way. This tool may be simple, but it introduces one of the core pillars of cybersecurity in a powerful and easy-to-grasp manner.

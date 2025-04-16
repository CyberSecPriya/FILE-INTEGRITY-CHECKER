import hashlib
import os

# Function to calculate the hash of a file
def get_file_hash(filename):
    hasher = hashlib.sha256()  # You can also use hashlib.md5()
    with open(filename, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()

# Save hash to a file
def save_hash(filename, hash_value):
    with open('hashes.txt', 'w') as f:
        f.write(f"{filename}:{hash_value}")

# Load saved hash from file
def load_saved_hash():
    if not os.path.exists('hashes.txt'):
        return None, None
    with open('hashes.txt', 'r') as f:
        data = f.read().split(':')
        return data[0], data[1]

# Main program
filename = input("Enter the filename to check: ")

if not os.path.exists(filename):
    print("File not found!")
else:
    current_hash = get_file_hash(filename)
    saved_filename, saved_hash = load_saved_hash()

    if saved_hash is None:
        print("No hash found, saving current hash...")
        save_hash(filename, current_hash)
    else:
        if current_hash == saved_hash:
            print("File is unchanged.")
        else:
            print("WARNING: File has been modified!")
            

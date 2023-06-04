import os
import shutil

def delete_file(file_path):
    os.remove(file_path)
    print(f"Deleted file: {file_path}")

def quarantine_file(file_path):
    quarantine_path = os.path.join("C:/Program Files/Antivirus/Quarantine", os.path.basename(file_path))
    shutil.move(file_path, quarantine_path)
    # Make the file not executable (permissions 0000) and hide the folder
    os.chmod(quarantine_path, 0o000)
    os.system(f'attrib +h "{os.path.dirname(quarantine_path)}"')
    print(f"Moved file to quarantine: {quarantine_path}")

def scan_directory(directory):
    hash_file_path = "C:/Program Files/Antivirus/hash.txt"
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if hash_matches(file_path, hash_file_path):
                print(f"Matching file found: {file_path}")
                action = input("Choose an action:\n1. Delete\n2. Quarantine\n3. Skip\n")
                if action == "1":
                    delete_file(file_path)
                elif action == "2":
                    quarantine_file(file_path)
                elif action == "3":
                    print("Skipped file.")
                else:
                    print("Invalid choice. Skipping file.")

def hash_matches(file_path, hash_file_path):
    # Compare file hashes
    # Replace this with your own code to calculate file hashes
    # and compare them with the contents of the hash_file_path
    return False

def main():
    print("1. Full Scan")
    print("2. Custom Scan")
    choice = input("Choose an option: ")

    if choice == "1":
        scan_directory("C:/")
    elif choice == "2":
        directory = input("Enter the directory path to scan: ")
        scan_directory(directory)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

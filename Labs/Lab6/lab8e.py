'''
Name: John Niagwan
ID: 121092225
'''
import sys
import os
import shutil

# Check if a command line argument is provided
if len(sys.argv) != 2:
    print("Usage: lab8e.py directory_name")
    sys.exit(1)

# Get the directory from the command line argument
target_directory = sys.argv[1]

# Check if the provided path is a valid directory
if not os.path.isdir(target_directory):
    print("Error: The specified path is not a valid directory.")
    sys.exit(1)

try:
    # Get the absolute path of the user-defined directory
    abs_directory = os.path.abspath(target_directory)
    
    # Create the backups directory if it doesn't exist
    backup_directory = os.path.join(abs_directory, 'backups')
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    
    # Iterate through files in the specified directory
    for root, _, filenames in os.walk(abs_directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)

            # Check if the file is a Python script (ends with .py)
            if filename.endswith('.py'):

                # Check if the file is not inside the backups directory
                if not file_path.startswith(backup_directory):
                    # Construct the destination path in the backups directory
                    destination_path = os.path.join(backup_directory, filename)

                    # Copy the Python script to the backups directory
                    shutil.copy(file_path, destination_path)
                    print(f"Copied: {filename} to backups directory.")

except Exception as e:
    print(f"An error occurred: {e}")

'''
Name: John Niagwan
Student ID: 121092225
'''
import sys
# Check if a filename is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: challenge6.py <filename>") # Print usage instructions if arguments are incorrect
else:
    filename = sys.argv[1] # Get the filename from the command-line arguments
    try:
        with open(filename, 'r') as file: # Open the specified file for reading
            lines = file.readlines() # Read all the lines from the file into a list    
            for letter in lines: # Iterate through each line in the list
                print(max(letter.lower())) # Convert the line to lowercase using .lower(), then find the maximum character and print it
    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
        sys.exit(1)
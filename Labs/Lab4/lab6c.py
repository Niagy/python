'''
Name: John Niagwan
Student ID: 121092225
'''
import sys
sys.argv.append("hello")
sys.argv.append("readme1.txt")
if len(sys.argv) != 3: # Check if the number of command-line arguments is not equal to 3
    print("Usage: lab6c.py keyword filename") # Print usage instructions if arguments are incorrect
else:
    keyword = sys.argv[1] # Get the keyword from the first command-line argument
    filename = sys.argv[2] # Get the filename from the second command-line argument
    try:
        with open(filename, 'r') as f: # Open the specified file for reading
            lines = f.readlines() # Read all the lines from the file into a list
        # Iterate through each line in the list, keeping track of line numbers starting from 1
        for linenumber, line in enumerate(lines,1):
            if keyword in line: # Check if the keyword is in the current line
                print(f"{linenumber}: {line.strip()}") # If found, print the line number and the line (stripped of leading/trailing spaces and newlines)
    except FileNotFoundError:
        print(f"ERROR: {filename} not found.") # Handle the case where the file is not found and print an error message
        sys.exit(1) # Exit the program with an error code of 1
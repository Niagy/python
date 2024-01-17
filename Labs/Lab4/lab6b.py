'''
Name: John Niagwan
Student ID: 121092225
'''
import sys # Import sys module

if len(sys.argv) == 1: # Check if cmd has an argument if not set filename to readme.txt
    filename = 'readme.txt'
else:
    filename = sys.argv[1] # If cmd has an argument, set filename to argument
try:
    with open(filename, 'r') as f: # Try block to open file in read mode
        lines = f.readlines() # Save each lines in file in line list using readlines()
    for line in reversed(lines): # Use reverse() to reverse list and iterate through it
        print(f"{line.strip()}") # print each line and strip \n
    f.close() # Close file
except:
    sys.exit(1) # Exception handling
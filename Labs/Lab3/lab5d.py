"""
Name: John Niagwan
Student ID: 121092225
"""
import sys # Import the sys module
 
print(sys.argv) # Print the list of command-line arguments
print(f"The name of the file you are running is: {sys.argv[0]}.") # Print the name of the file being executed (the first element in sys.argv)
 
if len(sys.argv) == 1: # Check if any command-line arguments were provided
    print("No arguments found.") 
else: 
    for arg in sys.argv[1:]: # Iterate through the command-line arguments (excluding the script name at index 0)

        print(f"Argument found: {arg}.") # Print each argument
print("Complete.") # Print "Complete"
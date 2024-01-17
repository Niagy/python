'''
Name: John Niagwan
ID: 121092225
Requirements 
- Use sys module to check if filename is present in command line argument
- open file in read mode
- Use readline() method to put lines in a list
- Create regex expressioon for phone numbers
- Use re.compile method to create regex
- Use findall to match numbers in lines list which has been coverted to string, save numbers in mo list
- Print number of matches found
- Ask user if they want to see results
- Use for loop to print matches
'''
import sys
import re

# Check if a filename is present in the command line arguments
if len(sys.argv) == 1:
    print("Usage: lab8b.py filename")
elif len(sys.argv) == 2:
    try:
        # Get the filename from the command line argument
        filename = sys.argv[1]

        # Open the file in read mode
        with open(filename, 'r') as f:
            # Read lines from the file and store them in a list
            lines = f.readlines()

        # Create a regex expression for phone numbers
        tel_num = re.compile(r'\d{3}-\d{3}-\d{4}')

        # Use findall to match numbers in the lines list
        mo = tel_num.findall(' '.join(lines))  # Join lines into a single string before searching

        # Print the number of matches found
        print(f"Number of matches found: {len(mo)}")

        # Ask the user if they want to see results
        answer = input("Would you like to see results (y/n): ")

        if answer.lower() == 'y' or answer == '':
            # Use a for loop to print the matches
            for match in mo:
                print('Found phone number: ' + match)
        elif answer.lower() == 'n':
            sys.exit(0)  # Exit without an error

    except FileNotFoundError:
        print(f'ERROR: {filename} was not found.')  # Error handling
        sys.exit(1)
    except PermissionError:
        print(f'You do not have permission to open {filename}.')  # Error handling
        sys.exit(1)
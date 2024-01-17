"""
Name: John Niagwan
Student ID: 121092225
"""
import sys

num = 0 # Initialize a counter for the number of valid numbers
sum = 0 # Initialize a variable to accumulate the sum of valid numbers

if len(sys.argv) == 1: # Check if there are no command-line arguments provided (only the script name)
    print('Usage: Enter one or more command line arguments.')
    sys.exit(1)  # Exit the script with a non-zero status code (indicating an error)
else:
    for arg in range(1, len(sys.argv)): # Loop through the command-line arguments starting from the second argument (index 1) to the length of the sys.argv list
        if sys.argv[arg].isdigit(): # Check if the argument is a digit (represents a number)
            sys.argv[arg] = int(sys.argv[arg]) # Convert the argument to an integer
            print(f"Number found: {sys.argv[arg]}")
            sum += sys.argv[arg] # Add the number to the sum
            num += 1 # Increment the count of valid numbers
            
        else:
            print(f"Error: {sys.argv[arg]} is not a number.") # Handle the case where the argument is not a valid number
    

print(f"Average for {num} numbers: {sum/num}") # Calculate and print the average of valid numbers
sys.exit(0) # Exit the script with a status code of 0 (indicating successful execution)
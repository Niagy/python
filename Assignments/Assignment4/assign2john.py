'''
Name: John Niagwan
Myseneca: jniagwan
ID: 121092225
Description: 
'''
import csv
import sys
import os

# Function to read a CSV file and return a list of dictionaries
def dict_reader(filename):
    list_of_dicts = []
    # Use a 'with' statement to ensure proper file handling
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts

# Function to print a list of dictionaries in a tabular format
def dict_printer(list_of_dicts):
    count = 1
    # Print column headers
    print("#", end= ' ')
    for key in list_of_dicts[0]:
        print(f"{key : ^27} ", end=' ')
    print("\n" + '=' * 81)
    
    # Print data in a tabular format
    for dicts in list_of_dicts:
        print(f"{count}", end=' ')
        count+=1
        for key, value in dicts.items():
            print(f"{value : ^27} ", end=' ')     
        print()

if __name__ == "__main__":
    Total_SalesTemplate = {'Item':None, 'Sales':None, 'Price per Item':None, 'Total':None}
    # Check for the correct number of command line arguments
    sys.argv.append('inventory.csv')
    if len(sys.argv) == 1:
        print("Usage: assign2.py filename")
    elif len(sys.argv) == 2:
        try:
            # Read the CSV file into a list of dictionaries
            list_of_dict = dict_reader(sys.argv[1])
            
            # Print the modified data in a tabular format
            dict_printer(list_of_dict)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
    while True:
        selection = input(f"Select a number (1-{len(list_of_dict)}) to indicate a sale, or 'e' to indicate end of day:")
        try:
            selection = int(selection)
            selection -= 1
            if 0 <= selection < len(list_of_dict):
                list_of_dict[selection]["Current Stock"] =int(list_of_dict[selection]["Current Stock"]) - 1
            elif selection > len(list_of_dict)-1:
                print("Invalid selection")
        except:
            if selection.lower() == 'e':
                break
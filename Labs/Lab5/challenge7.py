'''
John Niagwan
121092225
'''
import csv
import sys

# Function to read a CSV file and return a list of dictionaries
def dict_reader(filename):
    list_of_dicts = []
    # Use a 'with' statement to ensure proper file handling
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_of_dicts.append(row)
    return list_of_dicts

# Function to modify specific fields in a list of dictionaries
def modify_dict_list(list_of_dicts):
    for dict in list_of_dicts:
        # Modify specific fields based on conditions
        if dict['First Name'] == 'Christoper':
            dict['First Name'] = 'Chris'
        if dict['Last Name'] == 'Patal':
            dict['Last Name'] = 'Patel'
        if dict['Last Name'] == 'Smith':
            dict['Last Name'] = 'Nichols'
        if dict['Address'] == '81 Vanier':
            dict['Address'] = '72 Princeton'
        if dict['Last Name'] == 'Geary':
            dict['Address'] = '455 Bloor'
        if dict['City'] == 'North York':
            dict['City'] = 'Toronto'
        if 'Country' in dict and dict['Country'] == 'Canada':
            dict['Country'] = 'CA'

# Function to write a list of dictionaries to a CSV file
def dict_writer(filename, list_of_dicts):
    # Use a 'with' statement to ensure proper file handling
    with open(filename, 'w', newline='') as f:
        fieldnames = list_of_dicts[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)

# Function to print a list of dictionaries in a tabular format
def dict_printer(list_of_dicts):
    # Print column headers
    for key in list_of_dicts[0]:
        print(f"{key : <27} |", end=' ')
    print("\n" + '-' * 194)
    
    # Print data in a tabular format
    for dicts in list_of_dicts:
        for key, value in dicts.items():
            print(f"{value : <27} |", end=' ')
        print()

if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) == 1:
        print("Usage: lab7d.py filename")
    elif len(sys.argv) == 2:
        try:
            # Read the CSV file into a list of dictionaries
            list_of_dict = dict_reader(sys.argv[1])
            
            # Modify specific fields in the list of dictionaries
            modify_dict_list(list_of_dict)
            
            # Write the modified list of dictionaries back to the CSV file
            dict_writer(sys.argv[1], list_of_dict)
            
            # Print the modified data in a tabular format
            dict_printer(list_of_dict)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)

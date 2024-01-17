'''
Name: Thi Ngoc YEN, Tran
Student ID: 118828235
Description: [Lab 7d] Substitute Data In A CSV File
'''

import csv, sys, os

def read_csv(filename):
    "This function is to read the csv file"

    list_of_dicts = []
    f = open(filename, 'r')
    reader = csv.DictReader(f)
    for row in reader: # row {'id': '2', 'First Name': 'Meg'}

        # Substitue on some data of the file:
        if row['First Name'] == "Christopher":
            row['First Name'] = "Chris"
        if row['Last Name'] == "Patal":
            row['Last Name'] = "Patel"
        if row['Last Name'] == "Smith":
            row['Last Name'] = "Nichols"
        if row['Address'] == "81 Vanier":
            row['Address'] = "72 Princeton"
        if row['Last Name'] == "Geary":
            row['Address'] = "455 Bloor"
        if row['City'] == "North York":
            row['City'] = "Toronto"
        if 'Country' in row:
            if row['Country'] == "Canada":
                row['Country'] = "CA"
        
        # Append the row into the list_of_dicts list:
        list_of_dicts.append(row) 

    f.close()
    return list_of_dicts # list_of_dicts: [{'id': '1', 'First Name': 'Sophie'}, {'id': '2', 'First Name': 'Meg'},...]


def write_csv(new_filepath, list_of_dicts):
    "This function is to write to new csv file"

    fieldnames = list_of_dicts[0].keys()
    
    with open(new_filepath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in list_of_dicts:
            w.writerow(row)


if __name__ == "__main__":
    # If the user does not pass in any argument:
    if len(sys.argv) == 1: 
        print("ERROR: Please include one argument for the new filename.")

    #If the user passed in at least one argument, take the first argument as the new filename:
    else:
        # Call function to read csv:
        list_of_dicts = read_csv('test1.csv')

        # Call function to write to new csv file:
        new_filename = sys.argv[1]
        new_filepath = os.path.join('/Users/niagy/Desktop/SenecaBTT/PRG600/Labs/lab5', f'{new_filename}')
        write_csv(new_filepath,list_of_dicts)
'''
Name: John Niagwan
Student ID: 121092225
'''
data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!'] # Create list of string
f = open('testing.txt', 'w') # Open file testing.txt file with write permissiom
for i in range(len(data_to_write)): # Using i as index for each index in list
    f.write(f"{data_to_write[i]}\n") # Write to file on a new line
f.close() # Close file

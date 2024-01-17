"""
Name: John Niagwan
Student ID: 121092225
"""
bin_str = '' #initialise empty string
user_num = int(input("Enter a decimal number:")) #ask user to input a decimal(base 10) number
while user_num > 0: #while user input is greater than 0
    bit = user_num % 2 #divide user input by 2 and save remainder in bit variable
    user_num = user_num // 2 #divide user input by 2 and save in user_num variable
    bin_str = str(bit) + bin_str #add convert bit value to string and save in bin_str variable append new bit values every loop until loop ends
print(bin_str) #print string stored in bin_str which is the binary representation of the decimal number inputed ny user

print(bin(60)) #using bin() function to verify my code
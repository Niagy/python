"""
Name: John Niagwan
Student ID: 121092225
"""
from random import randint

secret = randint(1, 10) #Generate a random secret number between 1 and 10
user_input = (input("Guess a number between 1 and 10: ")) #Prompt the user to guess a number between 1 and 10

while user_input != secret: #Start a loop that continues until the user's guess matches the secret number
    if user_input.isnumeric() and 0 < int(user_input) < 11: # Check if the user's input is a numeric value between 1 and 10
        if int(user_input) != secret: #Check if the user's guess converted to integer is incorrect, print message and prompt to guess again
            print("Sorry. Try again.")
            user_input = input("Enter a number between 1 and 10: ")
        else: #if user guess is correct print message and break loop
            print("Correct! You win.")
            break
        
    else: #if invalid input is entered print error message and prompt user to guess again
        print("Error: not a number or out of bounds.")
        user_input = input("Enter a number between 1 and 10: ")



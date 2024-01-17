"""
Name: John Niagwan
Student ID: 121092225
"""
from random import randint #import randint function from random library

secret = randint(1, 10) #generate a secret random number between 1 and 10 using randint function
user_guess = int(input("Guess a number between 1 and 10: ")) #asks user to guess number

while user_guess != secret: #starts a while loop that continues until user get the right secret number
    if user_guess != secret:#if user guess is not equal to secret number print sorry
        print("Sorry, that's not it.") 
        user_guess = int(input("Guess a number between 1 and 10: ")) #asks user to input another guess
print("Correct! You win.") #when user gets the secret number lopp is exited and You win message is printed


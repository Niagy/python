"""
Name: John Niagwan
Student ID: 121092225
"""
import random # Import the random module

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ] # List of animal names
secret = random.choice(animals) # Randomly select a secret animal name from the list

print("I'm thinking of an animal. Can you guess what it is?") # Print a message to the user

while True: # Start an infinite loop
    user_guess = input("Enter a letter or a guess. Press enter to quit: ") # Prompt the user to enter a letter or a guess
    
    
    if user_guess == secret: # Check if the user's guess matches the secret animal name
        print("You Win!") # User guessed the correct animal and loop breaks
        break
    elif len(user_guess) == 1: # Check if the guess is a single letter
        if user_guess in secret: # Check if letter is in secret animal name
            print("Yes, my word contains that letter.") # If yes, print "yes" message and loop to input
        else:
            print("Sorry, my word doesn't contain that letter.") # If no, print sorry message and loop to input
    elif user_guess == "":
        break
    else:
        print("Sorry, that's not it.") # if animal is wrong print sorry message and loop to input      
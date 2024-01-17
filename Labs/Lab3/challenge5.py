"""
Name: John Niagwan
Student ID: 121092225
"""
import random

carmake = ['toyota', 'honda', 'bmw', 'kia', 'ford', 'mazda', 'nissan', 'tesla', 'hyundai', 'porsche' ] # Initialize car make list
secret_car = random.choice(carmake) # Randomly select a secret car make from the list
guessed_letters = [] # Initialize a list to store guessed letters

print("I'm thinking of a car make. Can you guess what it is?")

while True: #Start infinite loop to allow users to guess
    display_word = '' # Initialize an empty string to represent the guessed word
    for letter in secret_car: # For each letter in secret word
        if letter in guessed_letters: # If the letter exists in guessed_letters list
            display_word += letter + " " # Append guessed letters to the display word. On first loop it will be all "_" on subsequent loops if an inputted letter is in the list and also exsists in the secret_car then it will be added to display word
        else:
            display_word += "_ "  # Append underscores for unrevealed letters
    print("Your word:\n", display_word) # Display the current state of the guessed word to the user

    guess = input("Enter your guess: ") # Prompt the user for a guess

    if guess == secret_car: # If the user guessed the correct car make, they win the game and the loop ends
        print("You win!")
        break
    elif guess.isalpha() and len(guess) == 1: # Checks that the user's input is a single letter
        if guess not in guessed_letters: # If the letter doesn't exist already in the list it will be added to the list.
            guessed_letters.append(guess) # Append the guessed letter to the list of guessed letters
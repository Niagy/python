"""
Firstname: John
Lastname: Niagwan
Username: Jniagwan
StudentID: 121092225
Email: jniagwan@myseneca.ca
"""

import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    
    dice1 = randint(1, 6) # Generate random numbers for two dice faces (1 to 6).
    dice2 = randint(1, 6)    
    
    print(f"{dice1} and {dice2}") # Print the results of the dice rolls.
    
    total = dice1 + dice2 # Calculate the total by summing the two dice values.
    return total # return total

# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    while True:
        try:
            num_players = int(input("Enter the number of players: ")) # Ask the user for the number of players.
             
            if num_players <= 0: # Check if the user input is a positive number.
                print("Please enter a positive number of players.")
                continue
  
            players = [] # Iniialise empty player list
        
            for i in range(num_players):
                player_name = input(f"Please enter player #{i + 1} name: ") # Ask for player names based on the number of players.
                players.append(player_name)
            return players
        except ValueError:
            print("Invalid input please try again.") # Error message for invalid input

# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
    while True:
        try:
            roundcount = int(input("Please enter how many rounds the players wish to play: ")) #Prompt user for number of rounds players wish to play
            break # If the input is a valid integer, break out of the loop.
        except:
            print("Invalid input please try again") #If not integer print message and ask again
    return roundcount

# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here
    game = [[0] * roundcount for _ in players] # Initialize the 'game' list with zeros, representing scores for each player and each round.
    gameset = [game, players, roundcount]     # Create a 'gameset' list containing the 'game' list, 'players' list, and 'roundcount.'
    return gameset

# 1 Marks 
def asktoroll(player): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    # Implement your function here 
    input(f"{player}! Hit enter once you are ready to roll your dices!") # Ask the player to hit Enter to roll the dice.
    score = rolldice() # Call the 'rolldice' function to get the score.
    return score # Return score

# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    # Implement your function here
    max_score = max([sum(round_scores) for round_scores in game]) # Calculate the maximum score achieved by any player.
    winners = [players[i] for i, round_scores in enumerate(game) if sum(round_scores) == max_score] # Find the player(s) with the maximum score.
    return ",".join(winners) # Join the winning player(s) with commas if there are multiple winners.

# 5 Marks 
def rungame():
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players, and roundcount from setgame
    It prints the header and Round 1 beginning scorecard first with initial scores set to 0
    It then asks users to roll dice using asktoroll function for all rounds and players 
    When the game finishes, it prompts for continuation, and if chosen to continue, run the game again; otherwise, terminate.
    """

    # The next 5 lines are to get you started 
    # Implement the rest of the code 
    gameset = setgame()
    game = gameset[0]
    players = gameset[1]
    roundcount = gameset[2]
    
   
    roundnum = 0 # Initialize the round number to 0.

    while roundnum < roundcount: # Loop through each round.
        printgame(game, players, roundnum, roundcount)  # Print the current scorecard.
        for i, player in enumerate(players): # Ask each player to roll the dice and record their scores.
            score = asktoroll(player) 
            game[i][roundnum] = score
        roundnum += 1 # Move to the next round.

    # Print the final scoreboard
    printgame(game, players, roundcount, roundcount) # Print the final scoreboard

    winner = findwinner(game, players) # Find and announce the winner.
    print(f"Congratulation {winner}! You are our WINNER!")

    play_again = input("Do you want to play another game?\n[1]Yes\n[2]No\nYour Choice:") # Prompt for continuation or termination.
    if play_again == "1":
        rungame()
    else:
        print("Thanks for playing!")



# 5 Marks
def printgame(game, players, roundnum, roundcount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    if roundnum == 0: # If statement to print initial Round 1 "0" score table
        
        print(f"{'*' * 18} Round {1} {'*' * 18}")# Print the scorecard for the current round using f-string
        print(f"{'':<5}", end="")  # Initial spacing

        
        for i in range(1, roundcount + 1):# Print column headers for each round looping through from round 1 to roundcount + 1 to include the final round number
            print(f"Round {i:<2}", end="")

        print("Total")

        for i, player in enumerate(players): #For each player in players list
            print(f"{player:<10}", end="") # Print the player's name with a left alignment and a field width of 10 characters

            for j in range(roundcount):
                print(f"{game[i][j]:<7}", end="") # Print the player's score for the current round with left alignment and a field width of 7 characters

            total_score = sum(game[i][:roundnum]) # Calculate the player's total score for the rounds played so far
            print(f"{total_score:<7}") #Print player's total score

        print("*" * (19 + 7 * roundcount)) # print table * table boundary
    elif roundnum < roundcount: # elif statment to loop all rounds after the initial "0" score to the end of roundcount-1
        
        print(f"{'*' * 18} End of Round {roundnum} {'*' * 18}")# Print the scorecard for the current round
        print(f"{'':<5}", end="")

        
        for i in range(1, roundcount + 1):# Print column headers for each round
            print(f"Round {i:<2}", end="")

        print("Total")

        for i, player in enumerate(players):
            print(f"{player:<10}", end="")

            for j in range(roundcount):
                print(f"{game[i][j]:<7}", end="")

            total_score = sum(game[i][:roundnum])
            print(f"{total_score:<7}")
        print("*" * (19 + 7 * roundcount))
    else:
        # Print the final scoreboard after roundnum loop
        print(f"{'*' * 17} End of Round {roundnum} {'*' * 17}")
        print(f"{'':<5}", end="")  
   
        for i in range(1, roundcount + 1):# Print column headers for each round in the final scoreboard
            print(f"Round {i:<2}", end="")

        print("Total")

        for i, player in enumerate(players):
            
            print(f"{player:<10}", end="")# Print player names 

            for j in range(roundcount):
                
                print(f"{game[i][j]:<7}", end="")# Print scores 

            total_score = sum(game[i])
            
            print(f"{total_score:<7}")# Print total score
        print("*" * (18 + 7 * roundcount))


def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block
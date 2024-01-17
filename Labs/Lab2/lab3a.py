"""
Name: John Niagwan
Student ID: 121092225
"""
#Initialize variables to keep track of the current number and the user's score
num = 0  
point = 0

#First while loop to keep repeating question if the users answer is not equal to 26, it breaks if they skip which doesn't give a point or if they get the right answer which increases their point by 1
while num != 26: #while  num is not equals to 26 execute while loop
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ") #stores user input in variable user_input
    if user_input == 's': #if user input is equal to 's' loop breaks
        break 
    else: 
        num = int(user_input) #else value of user_input is converted to int and stored in num
    if num != 26: 
        print("Incorrect. Try again.") #if new num value is not equals to 26 print incorrect message
    else: 
        print("Correct! You have been awarded 1 point!") #else print correct message and increase point by 1
        point += 1

#Second question is printed and a while loop is used in the same way as the loop above
print("Enter the answer to 23 + 8, or press 's' to skip:")
while num != 31: 
    user_input = input() 
    if user_input == 's': 
        break 
    else: 
        num = int(user_input) 
    if num != 31: 
        print("Incorrect. Try again.") 
    else: 
        print("Correct! You have been awarded 1 point!")
        point += 1

#Third question is printed and a while loop is utlised in the same way as the previous two.
print("Enter the answer to 30 + 13, or press 's' to skip:")
while num != 43: 
    user_input = input() 
    if user_input == 's': 
        break 
    else: 
        num = int(user_input) 
    if num != 43: 
        print("Incorrect. Try again.") 
    else: 
        print("Correct! You have been awarded 1 point!")
        point += 1

#Fourth question is printed and a while loop is used until question is answered or skipped
print("Enter the answer to 17 + 27, or press 's' to skip:")
while num != 44: 
    user_input = input() 
    if user_input == 's': 
        break 
    else: 
        num = int(user_input) 
    if num != 44: 
        print("Incorrect. Try again.") 
    else: 
        print("Correct! You have been awarded 1 point!")
        point += 1

#Calculates the users grade % based on their points and prints the grade
grade = (point/4) * 100
print(f"You received a grade of {grade}%.")
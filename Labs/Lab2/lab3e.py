"""
Name: John Niagwan
Student ID: 121092225
"""
from random import randint #imports randint function from random library

num1 = randint(1, 10) #num1 varable initialised with a random number between 1 and 10
num2 = randint(1, 10) #num2 varable initialised with a random number between 1 and 10
sum = num1 + num2 #sum calculated from num1 and num2
user_input = "a" #user input initailised to "a"
point = 0 #point to keep score initialised to 0
question = 0 #question to keep number of questions answered of skipped
while user_input != "q": #starts a while loop until user enters 'q' to quit
    user_input = input(f"Enter the answer to {num1} + {num2}, press 's' to skip or 'q' to quit: ") #asks for answer of num1 + num2
    if user_input == 'q': #if user input is equals to q break loop
        break 
    elif user_input == 's': #else if user input is equal to s, print message and generate new values for num1, num2 and sum for new question. Increase question count by 1
        print("Question skipped. 0 points awarded.")
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        sum = num1 + num2
        question += 1 
    elif int(user_input) == sum: #else if user input converted to int is equal to sum, print message, increase point by 1, generate new values for num1, num2 and sum for new question and increase question count by 1
        print("Correct! You have been awarded 1 point!")
        print("Next question")
        point += 1
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        sum = num1 + num2
        question += 1 
    else: #if none of the above print incorrect message
        print("Incorrect. Try again.")


if user_input == 'q' and question == 0:#on quit perform check to avoid division by 0 error if q is entered at the begining
    question = 1 #if 'q' is pressed before any question is answered or skipped, make question equals to 1
    grade = (point/question) * 100 #calculate grade to 0.0% and print
    print(f"You received a grade of {grade:.1f}%.")
else: #else calcualte grade with number of points divded by total number of questions skipped or answered multiplied by 100 and print
    grade = (point/question) * 100
    print(f"You received a grade of {grade:.1f}%.")
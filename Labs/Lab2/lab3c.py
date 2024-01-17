"""
Name: John Niagwan
Student ID: 121092225
"""

sum = 0 #initalises variable to keep track of sum


print("SUMMING CALCULATOR") #prints title


while True: #uses True to start an infinite loop
    print("The sum so far: " + str(sum)) #prints current sum to user
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") #user input stored in variable user_input
    if user_input == "": #if user pressed "Enter" break loop
        break 
    else:  
        sum += int(user_input) #else convert user input into integer and add to sum and starts loop again
print("Thank you for using summing calculator. The final sum was " + str(sum) + ".") #displays a message with the final sum.
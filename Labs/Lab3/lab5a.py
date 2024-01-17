"""
Name: John Niagwan
Student ID: 121092225
"""
def my_sum(my_list): # Define my_sum function that takes a parameter
    total_sum = 0 # Initialize a variable to store the total sum
    for number in my_list: # Iterate through the list and add each number to the total_sum
        total_sum += int(number) 
    return total_sum # Return the total sum


if __name__ == "__main__": 
    user_numbers = [] # Initialize an empty list to store user input numbers
    print("AVERAGE CALCULATOR") # Print a title message
    while True: # Start infinite loop
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") # Prompt the user for input
        if user_input == "": # Check if the user pressed Enter (empty input) to exit the loop
            break 
        else:  
            user_numbers.append(int(user_input)) # Append the user's input (converted to an integer) to the user_numbers list
    num_sum = my_sum(user_numbers) # Calculate the sum of the user_numbers using the my_sum function
    
    # Print the total sum, total count, and calulate and print average
    print(f"Total sum is: {num_sum}. Total count is: {len(user_numbers)}. Average for this list is: {num_sum / len(user_numbers)}.") 
    print("Thank you for using average calculator.")
"""
Name: John Niagwan
Student ID: 121092225
"""
import math #import math library

def circle_area(radius): #define function to calculate area of circle with one parameter called radius
    
    return math.pi * (radius ** 2) #use the formula for the area of a cirlce using math.pi for value of pi


if __name__ == "__main__":
    
    print("Cirle Area Calculator")
    user_radius = input("Enter a radius between 0 and 1999: ") #prompt user to enter a radius between 0 and 1999
    if user_radius == '': #if user presses "Enter" on first propmt print "Program was cancelled"
        print("Program was cancelled.")
    else: #if not, execute while loop
        while True: #initialise infinite while loop
            if user_radius == '': #if user cancels program during loop print "Exiting..." and break loop
                print("Exiting...")
                break
            if user_radius.isdigit(): #checks if user input is numeric
                radius = float(user_radius) #converts user input to float
                if 0 < radius <= 1999: #checks if radius is withing range of 0 and 1999
                    area = circle_area(radius) #if yes, calculate area with function and radius inputed by user
                    print(f"Radius: {user_radius}. Area: {area}") #print radius and area
                    user_radius = input("Enter a radius between 0 and 1999: ") #prompt for another radius
                elif float(user_radius) > 1999: #else if user input is above 1999 pring error and prompt for new radius
                    print(f"Error: {user_radius} is out of range.")
                    user_radius = input("Enter a radius between 0 and 1999: ")
            else: #if user input is not numeric print error input is not a number and prompt for a new radius
                print(f"Error: {user_radius} is not a number.")
                user_radius = input("Enter a radius between 0 and 1999: ")
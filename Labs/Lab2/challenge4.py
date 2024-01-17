"""
Name: John Niagwan
Student ID: 121092225
"""
def rtrn_slope(x1, y1, x2, y2): #Define a function to calculate the slope between two points. It takes 4 parameters x and y coordinates of first point and x and y coordinates of second point
    return (y2 - y1) / (x2 - x1) #calulate slope using formula and returns value

check = True #initialise variable to control loop
while check: #start loop to get inputs and calculate first slope
    x1 = int(input("Enter the starting X value: "))
    y1 = int(input("Enter the next Y value: "))
    x2 = int(input("Enter the new X value: "))
    y2 = int(input("Enter the new Y value: "))
    if 0 < x1 < 11 and 0 < x2 < 11 and 0 < y1 < 11 and 0 < y2 < 11: #checks if all values are within range 1 to 10
        slope = rtrn_slope(x1, y1, x2, y2) #if yes, calculate slope using rtrn_slope function
        print(slope) #print slope
        check = False #change check to False to exit loop
    else: #if any of the 4 coordinates are not within range, ask user to input valid numbers again
        print("A number is out of bounds. Please enter 4 numbers between 1 and 10")

while True: #start infinte loop, break with ctrl + D
    y1 = y2 #store x2 and y2 values in x1 and y1 for new slope calculation
    x1 = x2
    x2 = int(input("Enter the new X value: ")) #prompt user for new x2 and y2 values 
    y2 = int(input("Enter the new Y value: "))
    slope = rtrn_slope(x1, y1, x2, y2) #calculate new slope with previous values of x2 and y2 with current values of x2 and y2
    print(slope) #print new slope

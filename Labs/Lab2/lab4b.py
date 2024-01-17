"""
Name: John Niagwan
Student ID: 121092225
"""
from random import randint 
 
def rtrn_area(length, width):  # there are two parameters length and width and they return a value of area
    "Calculates area by multiplying two parameters and returns the result" 
    return length * width 

 
 
def print_all_caps(name, age):  # there are two parameters name and age, no value is returned it only prints 
    """
    This function takes in two values name and age. the name value is converted to all caps with the upper() method and
    stored in a new variable called cap_name. It then prints a statement with the values stored in cap_name and age converted
    to string
    """ 
    cap_name = name.upper() 
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) 
+ ' YEARS OLD!!!') 
 
 
 
def get_rando():  # there are no parameters. it returns a value 
    "This function will generate and return a random integer between 1 and 101" 
    return randint(1, 101) 
 

 
def is_odd(num):  # there is one parameter num, it returns a True or False 
    """This function checks if a number is odd. It divides a number by 2 and if the remainder is equal to 1 it returns
       a True for an odd number and if the remainer is 0 it returns a False for an even number    
    """ 
    if num % 2 == 1: 
        return True 
    else:  
        return False 
 


if __name__ == "__main__": #put function calls in main
    print(is_odd(13)) 
    print(is_odd(get_rando())) 
# call the function again with new values
    print(is_odd(14)) 
    print(is_odd(get_rando()))

    lucky_num = get_rando()
    print(lucky_num) 
# call the function again with new values 
    secondlucky_num = get_rando()
    print(secondlucky_num)

    print_all_caps('eric', 41) 
    print_all_caps('melissa', 40) 
# call the function again with new values
    print_all_caps('John', 33)

    rect = rtrn_area(5, 3)
    print(rect) 
# call the function again with new values
    rect1 = rtrn_area(5,5)
    print(rect1)


"""
Name: John Niagwan
Student ID: 121092225
Description: Assignment1 Shopping Calculator
"""







discounted_item = ["candy", "eggs", "flour", "hummus", "ice cream", "chicken soup", "diapers"]
cart = []
total_cost = 0
total_saved = 0
print("Shopping Calculator")
item_count = 1
while True:
   

    item_name = input("Please enter an item of food, or press Enter to exit: ")
    if item_name == '':
        break
    else: 
        item_price = float(input(f"Item is: {item_name}. Please enter the price for this item: "))
        while True:
            try:
                item_quatity = int(input(f"Item is: {item_name}. Please enter the quantity for this item: "))
                break
            except:
                print("Invalid value. Try again")
        
        cart.append((item_count, item_name, item_price, item_quatity))
        item_count+=1



print("RECEIPT")
for item_count, item_name, item_quatity, item_price in cart:
    print(f"{item_count}. {item_name}      {item_quatity} x $ {item_price} =   $ {item_quatity*item_price:.2f}\n")

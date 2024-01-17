def get_item_name():
    while True:
        item_name = input("Please enter an item of food, or press Enter to exit: ")
        return item_name

def get_item_price():
    while True:
        item_price = input("Please enter the price for this item: ")
        try:
            item_price = float(item_price)
            break
        except:
                print("Error: price must be a number. Example: 1, or 1.99.")
    return item_price

def get_item_quantity():
    item_quantity = input("How many will you purchase: ")
    while not item_quantity.isdigit():
        print("Error: item count must be a positive whole number.")
        item_quantity = input("How many will you purchase: ")
        item_quantity = int(item_quantity)
    return int(item_quantity)

def calulator(cart):
    discounted_item = ["candy", "eggs", "flour", "hummus", "ice cream", "chicken soup", "diapers"]
    for sublist in cart:
        if isinstance(sublist, list) and sublist:
            item_name = sublist[1]
            if item_name in discounted_item:
                

     



if __name__ == "__main__":
    item_count = 1
    cart = []
    while True:
        name = get_item_name()
        if name == '':
            break
        price = get_item_price()
        quanity = get_item_quantity()
        cart.append((item_count, name, quanity, price))
        item_count += 1

    print("RECEIPT")
    for item_count, item_name, item_quantity, item_price in cart:
        print(f"{item_count}. {item_name}      {item_quantity} x $ {item_price} = $ {item_quantity * item_price}\n")

    
    
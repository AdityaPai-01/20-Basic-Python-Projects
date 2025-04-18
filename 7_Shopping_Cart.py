#Python Shopping Cart Program
#Features:
#   1. Add Items in cart.
#   2. Remove Items from cart.

Items_DB = ['Apples', 'Bananas', 'Grapes', 'Potatoes', 'Tomatoes', 'Onions', 'Meat', 'Egg', 'Milk']
Cart = []
is_running = True

while is_running:
    print("Welcome to PyShop!")
    print("We have following items in our shop:")
    print("-----------------------------------------------")
    for item in Items_DB:
        print(item, end=" | ")
    print()
    print()
    while True:
        Choice = input("What would you like to buy?(Q to quit): ").capitalize()
        if Choice in Items_DB:
            Cart.append(Choice)
            print(f"{Choice} were added to the cart!")
            print()
        elif Choice == "Q":
            is_running = False
            break   
        else:
            print("Please select from the above options.")
            print()
print("-----------------------------------------------")
print(f"Your cart: {Cart}")
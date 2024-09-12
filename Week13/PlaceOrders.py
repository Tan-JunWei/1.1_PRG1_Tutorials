# Tan Jun Wei
# S10266704C

prices = {'chicken' : 8.50,\
          'steak' : 13.80,\
          'fish' : 9.80,\
          'pasta' : 9.50,\
          'coffee' : 2.50,\
          'tea' : 1.80,\
          'water' : 0.50}

orders = {}
total_cost = 0

def options():
    # show menu
    print("-"*20)
    print('1. Add order')
    print('2. Summarize orders')
    print('3. Quit')
    print("-"*20)

def add_order(total_cost):
    # Prints out menu
    print(f'{"Item":<15}{"Price"}')
    print(f"{'----':<15}{'-----'}")
    for item, price in prices.items():
        print(f"{item.capitalize():<15}{price}")

    order = input("Your order? ").lower()

    if order in prices.keys():
        sets = int(input("How many sets? "))
        if order in orders:
            orders[order] += sets
        else:
            orders[order] = sets
        total_cost += prices[order] * sets
        print(f"{sets} sets of {order} ordered.")
    else:
        print(f"{order} is not available.")
    
    return total_cost

def summarize_orders():
    # Prints out summary
    print(f'{"Item":<15}{"Quantity"}')
    print(f"{'----':<15}{'--------'}")
    for item, quantity in orders.items():
        print(f"{item.capitalize():<15}{quantity}")
    print(f"Total cost = ${total_cost:.2f}")

while True:
    options()
    choice = input("Your choice? ")

    if choice == "3":
        break
    elif choice == "1":
        total_cost = add_order(total_cost)
    elif choice == "2":
        summarize_orders()
    else:
        print("Invalid choice. Try again.")

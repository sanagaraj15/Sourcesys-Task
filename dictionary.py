menu = {
    1: ("Pizza", 200),
    2: ("Burger", 100)
}
ordered_items = set()      
bill = 0

while True:
    print("----- Restaurant Bill -----")
    print("1. Pizza")
    print("2. Burger")
    print("3. Total Bill")
    print("4. Exit")
    
    choice = int(input("Enter Your Choice : "))
    
    if choice in menu:
        item_name, price = menu[choice]
        qty = int(input(f"You Ordered {item_name} and Enter Quantity : "))
        bill += qty * price
        ordered_items.add(item_name)   
        
    elif choice == 3:
        print("Ordered Items:", ordered_items)
        print("Your Total Bill =", bill)
        
    elif choice == 4:
        print("! Thank You Visit Again !")
        break
        
    else:
        print("Invalid Choice")

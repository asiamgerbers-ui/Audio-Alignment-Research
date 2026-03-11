def gerbers_cafe_payment_system():
    """Payment system for Gerbers Cafe (returns grand total including tax)"""
    
    drinks = {
        "black coffee": 3.00,
        "cappuccino": 4.00,
        "latte": 4.00,
        "mocha": 4.00,
        "espresso": 5.00,
        "tea": 3.00,
        "cocoa": 4.00,
        "energy drinks": 5.00,
        "bottled water": 3.00,
    }
    
    TAX_RATE = 0.085
    DOUBLE_SHOT = 2.00
    
    orders = []
    
    # Order drinks
    while True:
        choice = input("Select a drink (1 Black Coffee, 2 Cappuccino, 3 Latte, 4 Mocha, 5 Espresso, 6 Tea, 7 Cocoa, 8 Energy Drinks, 9 Bottled Water): ")
        drink_names = list(drinks.keys())
        
        if choice not in [str(i) for i in range(1, 10)]:
            print("Invalid choice. Please try again.")
            continue
        
        drink_name = drink_names[int(choice) - 1]
        drink_cost = drinks[drink_name]
        drink_addons = []
        addon_cost = 0.0
        double = False
        double_cost = 0.0
        
        # Ask for add-ons per drink
        if drink_name == "black coffee":
            sugar = input("Would you like to add sugar? (+$0.50) (y/n): ").lower() == "y"
            cream = input("Would you like to add cream? (+$0.50) (y/n): ").lower() == "y"
            if sugar:
                drink_addons.append("sugar")
                addon_cost += 0.50
            if cream:
                drink_addons.append("cream")
                addon_cost += 0.50
                
        if drink_name == "tea":
            honey = input("Would you like to add honey? (+$0.50) (y/n): ").lower() == "y"
            lemon = input("Would you like to add lemon? (+$0.50) (y/n): ").lower() == "y"
            if honey:
                drink_addons.append("honey")
                addon_cost += 0.50
            if lemon:
                drink_addons.append("lemon")
                addon_cost += 0.50
                
        if drink_name == "cocoa":
            marshmallows = input("Would you like to add marshmallows? (+$0.50) (y/n): ").lower() == "y"
            whipped_cream = input("Would you like to add whipped cream? (+$0.50) (y/n): ").lower() == "y"
            if marshmallows:
                drink_addons.append("marshmallows")
                addon_cost += 0.50
            if whipped_cream:
                drink_addons.append("whipped cream")
                addon_cost += 0.50
                
        if drink_name in ("cappuccino", "latte", "mocha"):
            dairy_free = input("Would you like to make it dairy-free? (+$0.50) (y/n): ").lower() == "y"
            if dairy_free:
                drink_addons.append("dairy-free milk")
                addon_cost += 0.50
            double_shot = input("Would you like to add a double shot? (+$2.00) (y/n): ").lower() == "y"
            if double_shot:
                double = True
                double_cost += DOUBLE_SHOT
                
        if drink_name == "energy drinks":
            options = input("Which energy drink would you like? (1 RedBull, 2 Monster): ")
            if options == "1":
                drink_name = "RedBull"
            elif options == "2":
                drink_name = "Monster"
            else:
                print("Invalid choice. Defaulting to RedBull.")
                drink_name = "RedBull"
        
        drink_total = drink_cost + addon_cost + double_cost
        
        order_item = {
            "drink": drink_name.title(),
            "base_price": drink_cost,
            "addons": drink_addons,
            "addon_cost": addon_cost,
            "double": double,
            "double_cost": double_cost,
            "total": drink_total  # total before tax
        }
        orders.append(order_item)
        
        another = input("\nWould you like to order another drink? (y/n): ").lower()
        if another != "y":
            break
    
    # Print receipt items and compute grand total
    print("\n" + "=" * 50)
    print("GERBERS CAFE - ITEMIZED RECEIPT")
    print("=" * 50)
    grand_total = 0.0
    for i, order in enumerate(orders, 1):
        line_total = order['total']
        tax = line_total * TAX_RATE
        total_with_tax = line_total + tax
        grand_total += total_with_tax
        
        print(f"\nDrink #{i}: {order['drink']} - ${order['base_price']:.2f}")
        if order['addons']:
            for addon in order['addons']:
                print(f"  + {addon.title()} - ${0.50:.2f}")
        if order['double']:
            print(f"  + Double Shot - ${DOUBLE_SHOT:.2f}")
        print(f"  Subtotal: ${line_total:.2f}")
        print("=" * 50)
    print(f"\nSubtotal for all drinks: ${grand_total / (1 + TAX_RATE):.2f}")    
    print(f" Tax (@{TAX_RATE*100:.1f}%): ${grand_total - (grand_total / (1 + TAX_RATE)):.2f}")
    print("=" * 50)
    print(f"GRAND TOTAL: ${grand_total:.2f}")
    print("=" * 50)
    print("\nThank you for your purchase at Gerbers Cafe!")
    
    return grand_total

# Run the payment system (this will return the grand total)
grand_total = gerbers_cafe_payment_system()
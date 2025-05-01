def hotel_menu():
    import sys
    original_stdout = sys.stdout

    with open('hotel_receipt.txt', 'w', encoding='utf-8') as f:
        sys.stdout = f

        print("Welcome to the Hotel")
        print("1. Masala Dosa - ₹120")
        print("2. Butter Dosa - ₹90")
        print("3. Idly - ₹80")
        print("4. Wada - ₹52")
        print("5. Exit")

        menu = {
            1: ("Masala Dosa", 120),
            2: ("Butter Dosa", 90),
            3: ("Idly", 80),
            4: ("Wada", 52)
        }

        total_transaction = 0

        while True:
            try:
                sys.stdout = original_stdout
                choice = int(input("Enter your choice (1-4) or 5 to exit: "))
                sys.stdout = f
                if choice == 5:
                    print("Thank you for visiting the hotel!")
                    break
                elif choice in menu:
                    sys.stdout = original_stdout
                    quantity = int(input(f"Enter the quantity of {menu[choice][0]}: "))
                    sys.stdout = f
                    item_total = menu[choice][1] * quantity
                    total_transaction += item_total
                    print(f"Your order for {quantity} {menu[choice][0]}(s) is confirmed. Total: ₹{item_total}")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"Total transaction for the day: ₹{total_transaction}")
        print("Thank you for visiting the hotel!")

        sys.stdout = original_stdout

hotel_menu()
# f.close()
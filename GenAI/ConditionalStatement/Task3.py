orders = []
while True:
    print("\n---Menu---")
    print("1. Add Order")
    print("2. Show orders and total")
    print("q. Quit")

    choice = input("Enter your choice (1,2,q): ")
    
    if choice == '1':
        order_amount = float(input("Enter the order amount: "))
        orders.append(order_amount)
        print(f"Order of ${order_amount:.2f} added.")
    elif choice == '2':
            total_revenue = 0
            print("\nOrder Amounts \tDiscount(%)\tFinal Amount")
            if orders.isnumeric():
                for amount in orders:
                    # apply discount rule
                    if amount >= 2000:
                        discount = 15
                    elif amount >= 1500 and amount < 2000:
                        discount = 10
                    elif amount >= 1000 and amount < 1500:
                        discount = 7
                    else:
                        discount = 0

                    # extra: add tax fixed 5 percent and print sub total; tax, final total still within 
                    # conditionals and basic arithmetic operations
                    discount_amount = amount * discount / 100  
                    sub_total = amount - discount_amount
                    tax = (sub_total * 5)/100
                    final_total = sub_total + tax
                    total_revenue += final_total
                    print(f"{amount:.2f}\t\t{discount}\t\t{final_total:.2f}")
    elif choice == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Try again.")  
        continue
      
def add_prices(price_list,price):
    price_list.append(price)
    print("Price List after adding price:", price_list)

def get_average_price(price_list):
   # print("Price List:", price_list)
    total = sum(price_list)
    average = total / len(price_list)
    return average

def get_max_price(price_list):
    return max(price_list)


prices = []
while True:
    print("\n------ Menu ------")
    print("1. Add Price")
    print("2. Show Average Price")
    print("3. Show Maximum Price")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        price = float(input("Enter the price to add: "))
        add_prices(prices, price)
        print(f"Price {price} added.")
    elif choice == '2':
        if prices:
            print("Prices:", prices)
            average_price = get_average_price(prices)
            print(f"Average Price: {average_price}")
        else:
            print("No prices available to calculate average.")
    elif choice == '3':
        if prices:    
            max_price = get_max_price(prices)
            print(f"Maximum Price: {max_price}")
        else:
            print("No prices available to find maximum.")
    elif choice == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
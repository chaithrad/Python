cart = []

while True:
    price_input = input("Enter the price of the item or press 'q' to quit: ")
    if price_input.lower() == 'q':
        break
    try:
        price = float(price_input)
        if price < 0:
            raise ValueError("Negative Price is not allowed.")
        cart.append(price)
    except ValueError as ve:
        print("Error:Invalid price", ve)

print("Total Items:", len(cart))
print("Total bill:", sum(cart))
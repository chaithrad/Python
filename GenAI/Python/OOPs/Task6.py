class product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product Name: {self.name}, Price: rs.{self.price}, Category: {self.category}"    

    def __add__ (self, other):
        return self.price + other.price

product1 = product("Laptop", 50000, "Electronics")
product2 = product("Smartphone", 10000, "Electronics")

print(product1)
print(product2)

total_price = product1 + product2
print(f"Total Price: rs.{total_price}")
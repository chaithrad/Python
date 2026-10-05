class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: rs.{self.price}")
        print(f"Category: {self.category}")

    def apply_discount(self, percentage):
        discount_price = self.price - (self.price * percentage / 100)
        return discount_price

product1 = Product("Laptop", 50000, "Electronics")   
product1.get_info()
print(f"Discounted Price: rs. {product1.apply_discount(10)}")
product2 = Product("Smartphone", 10000, "Electronics")
product2.get_info()
print(f"Discounted Price: rs. {product2.apply_discount(10)}") 
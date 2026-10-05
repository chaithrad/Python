class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be greater than zero.")

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: rs.{self.get_price()}")
        print(f"Category: {self.category}")
       


product1 = Product("Laptop", 50000, "Electronics")
product1.get_info()
print(f"Current Price: rs. {product1.get_price()}")
product1.set_price(45000)
product1.get_info()
print(f"Updated Price: rs. {product1.get_price()}") 
product1.set_price(-400) 
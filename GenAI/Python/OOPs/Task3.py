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
        print(f"Price: rs.{self.__price}")
        print(f"Category: {self.category}")

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty = warranty_years

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: rs.{self.get_price()}")
        print(f"Category: {self.category}")
        print(f"Warranty: {self.warranty} years")


product1 = ElectronicProduct("Laptop", 55000, "Electronics", 2)
product1.get_info()
print(f"\n")
product2 = Product("Smartphone", 15000, "Electronics")
product2.get_info()

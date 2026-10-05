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

class Laptop(Product):
    def __init__(self, name, price, category, ram, storage):
        self.name = name
        self.__price = price
        self.category = category
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: rs.{self.__price}")
        print(f"Category: {self.category}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB\n")

class Mobile(Product):
    def __init__(self, name, price, category, screen_size, battery_capacity):
        self.name = name
        self.__price = price
        self.category = category
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def get_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: rs.{self.__price}")
        print(f"Category: {self.category}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Battery Capacity: {self.battery_capacity} mAh")


laptop1 = Laptop("Dell XPS 13", 100000, "Electronics", 16, 512)
#laptop1.get_info()
#print(f"\n")
mobile1 = Mobile("Samsung Galaxy S21", 70000, "Electronics", 6.2, 4000)
#mobile1.get_info()

producta = [laptop1 , mobile1]

for product in producta:
    product.get_info()

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product Name: {self.name}, Price: rs.{self.price}, Category: {self.category}"

    def __add__ (self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_products(self,product):
        self.products.append(product)

    def remove_product(self,name):
        for product in self.products:
            if product.name == name:
                self.produts.remove(product)
                print("Product removed:",name)
                return
        print("Product not found")

    def get_total_value(self):
        total = 0

        for product in self.products:
            total = total+product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product)


class Store:
    def __init__(self,name):
        self.name = name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("ENter product price: "))
        category = input("Enter product category: ")

        product = Product(name,price,category)

        sel.Inventory.add_product(product)

    def show_summary(self):
        total_items = len(self,inventory.produts)
        total_value = self.inventory.get_total_value()

        print("Store: ", self.name)
        print("Total items: ",total_items)
        print("Total value: ", total_value)


store = Store("My Store")

store.add_new_product()
store.add_new_product()
store.add_new_product()

store.inventory.show_all_products()

store.show_summary()

product1 = store.inventory.products[0]
product2 = store.inventory.products[1]

total = product1+product2

print("Total Price: ", total)
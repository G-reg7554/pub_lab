class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def find_drink_by_name(self, drink_name):
        for drink_name
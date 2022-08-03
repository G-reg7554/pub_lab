class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.food = []

    def get_drink_by_name(self, name):
        for drink in self.drinks:
            if name == drink.name:
                return drink

    def increase_till(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        return customer.age >= 18

    def check_drunkness(self, customer):
        return customer.drunkness < 10

    def reduce_stock(self, drink):
        drink.stock -= 1

    def stock_value(self):
        value = 0
        for drink in self.drinks:
            value += drink.stock * drink.price
        return value

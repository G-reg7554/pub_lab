class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [ ]

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        return customer.age >= 18

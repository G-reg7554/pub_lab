from src.drink import *
from src.customer import *

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        return customer.age >= 18

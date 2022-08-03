from src.drink import *
from src.customer import *


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

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

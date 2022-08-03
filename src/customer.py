from src.pub import *
from src.drink import *


class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def increase_drunkness(self,drink):
        # increse drunkess from drink type
        self.drunkness += drink.alcohol_level

    def buy_drink(self, drink, pub):
        if pub.check_age(self) == False or pub.check_drunkness(self) == False:
            return
        else:
            self.reduce_wallet(drink)
            pub.increase_till(drink)
            self.increase_drunkness(drink)

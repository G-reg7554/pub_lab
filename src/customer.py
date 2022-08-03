from src.pub import *
from src.drink import *


class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drink(self, drink, pub):
        if pub.check_age(self) == False:
            print("Sorry pal, you're too young")
            return
        else:
            self.reduce_wallet(drink)
            pub.increase_till(drink)

from src.pub import *

class Customer:
    pass

    def __init__(self,name,wallet,age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_drink(self,drink,pub):
        self.wallet -= drink.price
        pub.increase_till(drink.price)


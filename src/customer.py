from src.pub import *

class Customer:
    pass

    def __init__(self,name,wallet,age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_drink(self,drink,pub):
        if pub.check_age(self) == False:
            print("Sorry pal, you're too young")
            return 
        else:
            self.wallet -= drink.price
            pub.increase_till(drink.price)
    
    


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

    def decrease_drunkness(self,food):
        self.drunkness -= food.rejuvenation_level

    def buy_drink(self, drink, pub):
        if pub.check_age(self) == False or pub.check_drunkness(self) == False:
            return
        elif drink.stock < 1:
            return
        else:
            self.reduce_wallet(drink)
            pub.increase_till(drink)
            self.increase_drunkness(drink)
            pub.reduce_stock(drink)

    def buy_food(self, food, pub):
        self.decrease_drunkness(food)
        self.reduce_wallet(food)
        pub.increase_till(food)


import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Dave", 50, 19)
        self.customer2 = Customer("Steph", 30, 12)
        self.drink = Drink("Beer", 5.50, 2, 14)
        self.pub = Pub("The Prancing Pony", 100)
        self.food = Food("Burger", 15, 2)

    def test_buy_drink(self):
        pub = Pub("The Prancing Pony", 100)
        drink = Drink("Gin and tonic", 5, 2, 14)
        self.customer1.buy_drink(drink, pub)
        self.assertEqual(45, self.customer1.wallet)
        self.assertEqual(105, pub.till)

    def test_buy_drink_too_young(self):
        pub = Pub("The Prancing Pony", 100)
        drink = Drink("Gin and tonic", 5, 2, 14)
        self.customer2.buy_drink(drink, pub)
        self.assertEqual(30, self.customer2.wallet)
        self.assertEqual(100, pub.till)

    def test_increase_drunkness(self):
        drink = Drink("Beer", 5.50, 2, 14)
        self.customer1.increase_drunkness(drink)
        self.assertEqual(2, self.customer1.drunkness)

    def test_buy_drink_not_drunk(self):
        self.customer1.drunkness = 8
        self.customer1.buy_drink(self.drink, self.pub)
        self.assertEqual(10, self.customer1.drunkness)
        self.assertEqual(13, self.drink.stock)

    def test_buy_drink_too_drunk(self):
        self.customer1.drunkness = 32
        self.customer1.buy_drink(self.drink, self.pub)
        self.assertEqual(32, self.customer1.drunkness)
        self.assertEqual(14, self.drink.stock)

    def test_buy_food(self):
        self.customer1.drunkness = 8
        self.customer1.buy_food(self.food, self.pub)
        self.assertEqual(6, self.customer1.drunkness)
        self.assertEqual(35, self.customer1.wallet)
        self.assertEqual(115, self.pub.till)

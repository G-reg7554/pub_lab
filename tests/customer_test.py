import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Dave", 50, 19)
        self.customer2 = Customer("Steph", 30, 12)

    def test_buy_drink(self):
        pub = Pub("The Prancing Pony", 100)
        drink = Drink("Gin and tonic", 5)
        self.customer1.buy_drink(drink, pub)
        self.assertEqual(45, self.customer1.wallet)
        self.assertEqual(105, pub.till)

    def test_buy_drink_too_young(self):
        pub = Pub("The Prancing Pony", 100)
        drink = Drink("Gin and tonic", 5)
        self.customer2.buy_drink(drink, pub)
        self.assertEqual(30, self.customer2.wallet)
        self.assertEqual(100, pub.till)

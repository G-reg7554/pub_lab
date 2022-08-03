import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 50,37)

    def test_buy_drink(self):
        pub = Pub("The Prancing Pony", 100)
        drink = Drink("Gin and tonic", 5)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(105, pub.till)

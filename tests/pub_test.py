import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        drink1 = Drink("Beer", 5.50, 2,14)
        drink2 = Drink("Wine", 8, 1,14)
        drink3 = Drink("Gin", 6.50, 3,14)
        self.pub.drinks.append(drink1)
        self.pub.drinks.append(drink2)
        self.pub.drinks.append(drink3)
        food1 = Food("Burger", 15, 2)
        self.pub.food.append(food1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        drink = Drink("Gin and tonic", 5, 2, 14)
        self.pub.increase_till(drink)
        self.assertEqual(105, self.pub.till)

    def test_check_age_old_enough(self):
        customer = Customer("Dave", 130, 54)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age_too_young(self):
        customer = Customer("Steph", 130, 16)
        self.assertEqual(False, self.pub.check_age(customer))

    def test_stock_value(self):
        self.assertEqual(280,self.pub.stock_value())

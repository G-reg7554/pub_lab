import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.5)
        self.assertEqual(102.5, self.pub.till)
    
    def test_check_age_old_enough(self):
        customer = Customer("Dave",130, 54)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_age_too_young(self):
        customer = Customer("Steph", 130, 16)
        self.assertEqual(False, self.pub.check_age(customer))

import unittest

from customerrecords.models import Customer, Location


class TestCustomerModel(unittest.TestCase):

    def setUp(self):
        self.location = Location(50.0, 50.0)

    def test_valid_customer(self):
        customer = Customer(34, "John Snow", self.location)
        self.assertEqual(customer.id, 34)
        self.assertEqual(customer.name, "John Snow")
        self.assertEqual(customer.location, self.location)

    def test_str_id(self):
        customer = Customer("34", "John Snow", self.location)
        self.assertEqual(customer.id, 34)
        self.assertEqual(customer.name, "John Snow")
        self.assertEqual(customer.location, self.location)

    def test_empty_id(self):
        with self.assertRaises(ValueError):
            Customer("", "John Snow", self.location)

    def test_int_name(self):
        with self.assertRaises(ValueError):
            Customer(34, 23, self.location)

    def test_empty_name_1(self):
        with self.assertRaises(ValueError):
            Customer(34, "", self.location)

    def test_empty_name_2(self):
        with self.assertRaises(ValueError):
            Customer(34, "      ", self.location)

    def test_other_type_location(self):
        with self.assertRaises(ValueError):
            Customer("34", "John Snow", 78)


if __name__ == '__main__':
    unittest.main()

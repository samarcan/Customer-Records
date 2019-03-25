import unittest

from customerrecords.models import Location, Headquarter

class TestHeadquarterModel(unittest.TestCase):

    def setUp(self):
        self.location = Location(50.0, 50.0)
    
    def test_valid_headquarter(self):
        headquarter = Headquarter("Awesome Headquarter", self.location)
        self.assertEqual(headquarter.name, "Awesome Headquarter")
        self.assertEqual(headquarter.location, self.location)
    
    def test_int_name(self):
        with self.assertRaises(ValueError):
            headquarter = Headquarter(23, self.location)
    
    def test_empty_name_1(self):
        with self.assertRaises(ValueError):
            headquarter = Headquarter("", self.location)
    
    def test_empty_name_2(self):
        with self.assertRaises(ValueError):
            headquarter = Headquarter("      ", self.location)

    def test_other_type_location(self):
        with self.assertRaises(ValueError):
            headquarter = Headquarter("Awesome Headquarter", 78)


if __name__ == '__main__':
    unittest.main()
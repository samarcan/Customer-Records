import unittest

import context

from models import Location, Headquarter


class TestHeadquarterModel(unittest.TestCase):

    def setUp(self):
        self.location = Location(50.0, 50.0)

    def test_valid_headquarter(self):
        headquarter = Headquarter("Awesome Headquarter", self.location)
        self.assertEqual(headquarter.name, "Awesome Headquarter")
        self.assertEqual(headquarter.location, self.location)

    def test_int_name(self):
        with self.assertLogs() as cm:
            Headquarter(23, self.location)
            self.assertIn("Name must be a string.", cm.output[0])

    def test_empty_name_1(self):
        with self.assertLogs() as cm:
            Headquarter("", self.location)
            self.assertIn("Name must not be empty.", cm.output[0])

    def test_empty_name_2(self):
        with self.assertLogs() as cm:
            Headquarter("      ", self.location)
            self.assertIn("Name must not be empty.", cm.output[0])

    def test_other_type_location(self):
        with self.assertLogs() as cm:
            Headquarter("Awesome Headquarter", 78)
            self.assertIn("Location must be a Location object.", cm.output[0])


if __name__ == '__main__':
    unittest.main()

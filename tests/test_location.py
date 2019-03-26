import unittest

from customerrecords.models import Location


class TestLocationModel(unittest.TestCase):

    def test_valid_location(self):
        location = Location(40.0, 50.0)
        self.assertEqual(location.longitude, 50.0)
        self.assertEqual(location.latitude, 40.0)

    def test_string_input(self):
        location = Location("40.0", "50.0")
        self.assertEqual(location.longitude, 50.0)
        self.assertEqual(location.latitude, 40.0)

    def test_int_input(self):
        location = Location(40, 50)
        self.assertEqual(location.longitude, 50.0)
        self.assertEqual(location.latitude, 40.0)

    def test_empty_latitude(self):
        with self.assertRaises(ValueError):
            Location("", 50)

    def test_empty_longitude(self):
        with self.assertRaises(ValueError):
            Location(50, "")

    def test_longitude_out_of_range(self):
        with self.assertRaises(ValueError):
            Location(-250.0, 50.0)

    def test_latitude_out_of_range(self):
        with self.assertRaises(ValueError):
            Location(50.0, -250.0)


if __name__ == '__main__':
    unittest.main()

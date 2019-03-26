import unittest

from customerrecords.models import Location
from customerrecords.utils.distancecalculator import DistanceCalculator


class TestDistanceCalculator(unittest.TestCase):
    def setUp(self):
        self.distanceCalculator = DistanceCalculator()

    def test_distance_calculator(self):
        barcelona = Location(41.38879, 2.15898)
        dublin = Location(53.3434, -6.26761)
        distance = self.distanceCalculator.betweenTwoLocations(
            barcelona, dublin)
        self.assertGreater(distance, 1400)


if __name__ == '__main__':
    unittest.main()

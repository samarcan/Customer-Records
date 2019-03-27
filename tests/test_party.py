import unittest

import context

from models import Customer, Headquarter, Location, Party


class TestPartyModel(unittest.TestCase):
    def setUp(self):
        self.customers = [
            Customer(1, 'Superman', Location(41.319425, 2.092161)),
            Customer(2, 'Batman', Location(43.601591, 1.450023)),
            Customer(3, 'WonderWoman', Location(41.445999, 2.225853)),
            Customer(4, 'Flash', Location(38.713367, -9.142088)),
        ]
        self.headquarter = Headquarter(
            "DC Headquarters", Location(41.418598, 2.182712))

    def test_create_party(self):
        party = Party(self.headquarter, 100)
        self.assertEquals(type(party), Party)

    def test_valid_guest(self):
        party = Party(self.headquarter, 100)
        self.assertEqual(party.checkValidGuest(self.customers[0]), True)
        self.assertEqual(party.checkValidGuest(self.customers[1]), False)
        self.assertEqual(party.checkValidGuest(self.customers[2]), True)
        self.assertEqual(party.checkValidGuest(self.customers[3]), False)
        self.assertEqual(party.checkValidGuest("test"), False)

    def test_add_guests(self):
        party = Party(self.headquarter, 100)
        party.addGuest(self.customers[0])
        party.addGuest(self.customers[1])
        party.addGuest(self.customers[2])
        party.addGuest(self.customers[3])
        self.assertEqual(party._guests, [self.customers[0], self.customers[2]])

    def test_sort_guests(self):
        party = Party(self.headquarter, 100)
        party.addGuest(self.customers[0])
        party.addGuest(self.customers[2])
        party.sortGuests('id', 'asc')
        self.assertEqual(party._guests, [self.customers[0], self.customers[2]])
        party.sortGuests('id', 'desc')
        self.assertEqual(party._guests, [self.customers[2], self.customers[0]])


if __name__ == '__main__':
    unittest.main()

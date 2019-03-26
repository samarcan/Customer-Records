from ..utils.distancecalculator import DistanceCalculator

from .customer import Customer


class Party():

    def __init__(self, headquarter, distanceFilter):
        self._headquarter = headquarter
        self._distanceFilter = distanceFilter
        self._guests = []
        self._distanceCalculator = DistanceCalculator()

    @property
    def headquarter(self):
        return self._headquarter

    @property
    def distanceFilter(self):
        return self._distanceFilter

    @property
    def guests(self):
        return self._guests

    def addGuest(self, guest):
        if self.checkValidGuest(guest):
            self._guests.append(guest)

    def sortGuests(self, field, order=None):
        reversedSort = True if order.lower() == 'desc' else False
        self.guests.sort(key=lambda x: getattr(
            x, field), reverse=reversedSort)

    def checkValidGuest(self, guest):
        if self._checkTypeGuest(guest):
            if self._checkGuestDistance(guest):
                return True
        return False

    def _checkTypeGuest(self, guest):
        return type(guest) is Customer

    def _checkGuestDistance(self, guest):
        distance = self._distanceCalculator.betweenTwoLocations(
            guest.location, self._headquarter.location)
        return distance <= self._distanceFilter

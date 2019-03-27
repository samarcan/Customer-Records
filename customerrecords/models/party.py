from utils.distancecalculator import DistanceCalculator
from models.basemodel import BaseModel

from models.customer import Customer


class Party(BaseModel):

    def __init__(self, headquarter, distanceFilter):
        super(Party, self).__init__()
        try:
            self._headquarter = headquarter
            self._distanceFilter = self.__validateDistanceFilter(
                distanceFilter)
            self._guests = []
            self._distanceCalculator = DistanceCalculator()
        except Exception as e:
            self.logger.critical(str(e))
            raise e

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
        order = order if order is not None else "ASC"
        self.logger.info("Sorting guests by %s in order %s" %
                         (field, order))
        reversedSort = True if order.lower() == 'desc' else False
        self.guests.sort(key=lambda x: getattr(
            x, field), reverse=reversedSort)

    def checkValidGuest(self, guest):
        try:
            self.__checkTypeGuest(guest)
            if self.__checkGuestDistance(guest):
                self.logger.info("Customer %d has been invited." % guest.id)
                return True
            self.logger.info("Customer %d has not been invited." % guest.id)
        except ValueError as e:
            self.logger.error("Guest" + str(e))
        return False

    def __validateDistanceFilter(self, distanceFilter):
        try:
            longitude = self.floatChecker(distanceFilter)
            self.greaterEqualThanChecker(distanceFilter, 0)
            return longitude
        except ValueError as e:
            raise type(e)("Distance filter" + str(e))

    def __checkTypeGuest(self, guest):
        self.objectTypeChecker(guest, Customer)

    def __checkGuestDistance(self, guest):
        distance = self._distanceCalculator.betweenTwoLocations(
            guest.location, self._headquarter.location)
        self.logger.info("Customer %d is %.2f km away "
                         "from the headquarter %s." % (guest.id, distance,
                                                       self._headquarter.name))
        return distance <= self._distanceFilter

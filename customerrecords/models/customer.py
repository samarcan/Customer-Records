from ..utils.baselog import BaseLog
from .location import Location


class Customer(BaseLog):
    def __init__(self, id, name, location):
        super(Customer, self).__init__()
        try:
            self._id = self.__validateId(id)
            self._name = self.__validateName(name)
            self._location = self.__validateLocation(location)
        except Exception as e:
            self.logger.warning(str(e))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    def __validateLocation(self, location):
        if type(location) is Location:
            return location
        else:
            raise ValueError("Location must be a Location object.")

    def __validateName(self, name):
        if type(name) is str:
            if name.strip() != "":
                return name
            raise ValueError("Name must not be empty.")
        raise ValueError("Name must be a string.")

    def __validateId(self, id):
        try:
            return self.__intChecker(id)
        except ValueError as e:
            raise type(e)("Id" + str(e))

    def __checkPositive(self, value):
        if value < 0:
            raise ValueError(" must be a positive number")

    def __intChecker(self, value):
        try:
            if type(value) is not int:
                return int(value)
            return value
        except ValueError as e:
            raise type(e)(" must be an int type.")

from models.location import Location
from models.basemodel import BaseModel


class Customer(BaseModel):

    def __init__(self, id, name, location):
        super(Customer, self).__init__()
        try:
            self._id = self.__validateId(id)
            self._name = self.__validateName(name)
            self._location = self.__validateLocation(location)
            self.logger.info("Created customer with id: %d" % self._id)
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
        try:
            return self.objectTypeChecker(location, Location)
        except ValueError as e:
            raise type(e)("Location" + str(e))

    def __validateName(self, name):
        try:
            return self.stringChecker(name)
        except ValueError as e:
            raise type(e)("Name" + str(e))

    def __validateId(self, id):
        try:
            id = self.intChecker(id)
            self.greaterEqualThanChecker(id, 0)
            return id
        except ValueError as e:
            raise type(e)("Id" + str(e))

from models.location import Location
from models.basemodel import BaseModel


class Headquarter(BaseModel):

    def __init__(self, name, location):
        super(Headquarter, self).__init__()
        try:
            self._name = self.__validateName(name)
            self._location = self.__validateLocation(location)
            self.logger.info("Created headquarter with name: %s" % self._name)
        except Exception as e:
            self.logger.critical(str(e))
            raise e

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

from models.location import Location
from utils.baselog import BaseLog


class Headquarter(BaseLog):
    def __init__(self, name, location):
        super(Headquarter, self).__init__()
        try:
            self._name = self.__validateName(name)
            self._location = self.__validateLocation(location)
            self.logger.info("Created headquarter with name: %s" % self._name)
        except Exception as e:
            self.logger.warning(str(e))

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

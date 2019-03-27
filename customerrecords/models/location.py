from models.basemodel import BaseModel


class Location(BaseModel):
    def __init__(self, latitude, longitude):
        self._latitude = self.__validateLatitude(latitude)
        self._longitude = self.__validateLongitude(longitude)

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __validateLongitude(self, longitude):
        try:
            longitude = self.floatChecker(longitude)
            self.rangeChecker(longitude, -180.0, 180.0)
            return longitude
        except ValueError as e:
            raise type(e)("Longitude" + str(e))

    def __validateLatitude(self, latitude):
        try:
            latitude = self.floatChecker(latitude)
            self.rangeChecker(latitude, -90.0, 90.0)
            return latitude
        except ValueError as e:
            raise type(e)("Latitude" + str(e))

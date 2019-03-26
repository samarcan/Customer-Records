

class Location():
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
            longitude = self.__floatChecker(longitude)
            self.__rangeChecker(longitude, -180.0, 180.0)
            return longitude
        except ValueError as e:
            raise type(e)("Longitude" + str(e))

    def __validateLatitude(self, latitude):
        try:
            latitude = self.__floatChecker(latitude)
            self.__rangeChecker(latitude, -90.0, 90.0)
            return latitude
        except ValueError as e:
            raise type(e)("Latitude" + str(e))

    def __rangeChecker(self, value, minVal, maxVal):
        if minVal > value or maxVal < value:
            raise ValueError(" must be between {minVal} and {maxVal}.".format(
                minVal=minVal, maxVal=maxVal))

    def __floatChecker(self, value):
        try:
            if type(value) is not float:
                return float(value)
            return value
        except ValueError as e:
            raise type(e)(" must be a float type.")

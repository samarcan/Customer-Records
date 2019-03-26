import math


class DistanceCalculator():

    def __init__(self):
        self._earthRadiusKm = 6371

    def betweenTwoLocations(self, loc1, loc2):
        return self.__calculateDistance(loc1.latitude, loc1.longitude,
                                        loc2.latitude, loc2.longitude)

    def __calculateDistance(self, lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
            math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return c * self._earthRadiusKm

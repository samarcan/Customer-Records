from utils.baselog import BaseLog


class BaseModel(BaseLog):

    def __init__(self):
        super(BaseModel, self).__init__()

    def stringChecker(self, value):
        if type(value) is str:
            if value.strip() != "":
                return value
            raise ValueError(" must not be empty.")
        raise ValueError(" must be a string.")

    def floatChecker(self, value):
        try:
            if type(value) is not float:
                return float(value)
            return value
        except ValueError as e:
            raise type(e)(" must be a float type.")

    def objectTypeChecker(self, obj, objType):
        if type(obj) is not objType:
            raise ValueError(" must be a %s object." % objType.__name__)
        return obj

    def intChecker(self, value):
        try:
            if type(value) is not int:
                return int(value)
            return value
        except ValueError as e:
            raise type(e)(" must be an int type.")

    def rangeChecker(self, value, minVal, maxVal):
        if minVal > value or maxVal < value:
            raise ValueError(" must be between {minVal} and {maxVal}.".format(
                minVal=minVal, maxVal=maxVal))

    def lessEqualThanChecker(self, value, maxVal):
        if maxVal < value:
            raise ValueError(" must be smaller than {maxVal}.".format(
                maxVal=maxVal))

    def greaterEqualThanChecker(self, value, minVal):
        if minVal > value:
            raise ValueError(" must be bigger than {minVal}.".format(
                minVal=minVal))

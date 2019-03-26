import os
import json


class DataReader():
    def __init__(self, filePath):
        self._filePath = self.__checkFilePath(filePath)

    def readData(self):
        with open(self._filePath, 'r') as dataFile:
            line = dataFile.readline()
            while line:
                yield json.loads(line)
                line = dataFile.readline()

    def __checkFilePath(self, filePath):
        if os.path.isfile(filePath):
            return filePath
        else:
            raise FileNotFoundError("File not found")

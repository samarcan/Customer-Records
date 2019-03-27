import os
import json
from json.decoder import JSONDecodeError
from .baselog import BaseLog


class DataReader(BaseLog):
    def __init__(self, filePath):
        super(DataReader, self).__init__()
        self._filePath = self.__checkFilePath(filePath)

    def readData(self):
        with open(self._filePath, 'r') as dataFile:
            line = dataFile.readline()
            while line:
                yield self.__decodeJsonLine(line)
                line = dataFile.readline()
    
    def __decodeJsonLine(self, line):
        try:
            self.logger.info("Reading line: %s", line.strip())
            return json.loads(line)
        except JSONDecodeError as e:
            self.logger.warning("Line must be in JSON format")

    def __checkFilePath(self, filePath):
        if os.path.isfile(filePath):
            return filePath
        else:
            self.logger.error("Data file does not exist.")
            raise FileNotFoundError("File not found")

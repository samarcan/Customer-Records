import unittest
import os
import json

from customerrecords.utils.datareader import DataReader


class TestDataReader(unittest.TestCase):
    def setUp(self):
        self.filePath = os.path.join(
            os.path.dirname(__file__), './example_data.txt')
        self.arrExampleData = [
            {'field1': 'value1'}, {'field2': 'value2'}, {'field3': 'value3'},
            {'field4': 'value4'}, {'field5': 'value5'}, {'field6': 'value6'}]
        with open(self.filePath, 'w+') as fileData:
            fileData.write('\n'.join([json.dumps(data)
                                      for data in self.arrExampleData]))

    def tearDown(self):
        os.remove(self.filePath)

    def test_create_datareader(self):
        dataReader = DataReader(self.filePath)
        self.assertEqual(type(dataReader), DataReader)

    def test_no_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            DataReader(os.path.join(
                os.path.dirname(__file__), './no_existing_file.txt'))

    def test_read_data(self):
        dataReader = DataReader(self.filePath)
        arrReadedData = [lineData for lineData in dataReader.readData()]
        self.assertEqual(arrReadedData, self.arrExampleData)


if __name__ == "__main__":
    unittest.main()

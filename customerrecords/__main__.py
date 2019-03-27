from models import Customer, Location, Headquarter, Party
from utils.datareader import DataReader


DEFAULT_KM_FILTER = 100.0
DEFAULT_FILE_PATH = "assets/customers.txt"


def createCustomer(data):
    latitude = data.get('latitude', '')
    longitude = data.get('longitude', '')
    userId = data.get('user_id', '')
    userName = data.get('name', '')
    location = Location(latitude, longitude)
    return Customer(userId, userName, location)


def printPartyGuests(party):
    for guest in party.guests:
        print("Id: {id}\tName: {name}".format(id=guest.id, name=guest.name))


def receiveInput():
    fileDataPath = input(
        "Insert path of customer data "
        "file (default='%s'): " % DEFAULT_FILE_PATH)
    kmFilter = input(
        "Insert radius in km where "
        "find the guests (default=%.2f): " % DEFAULT_KM_FILTER)
    kmFilter = float(kmFilter) if kmFilter != '' else DEFAULT_KM_FILTER
    fileDataPath = fileDataPath if fileDataPath != '' else DEFAULT_FILE_PATH
    return kmFilter, fileDataPath


if __name__ == '__main__':
    try:
        kmFilter, fileDataPath = receiveInput()
        hqLocation = Location(53.339428, -6.257664)
        headquarter = Headquarter('Intercom Dublin', hqLocation)
        party = Party(headquarter, kmFilter)
        dataReader = DataReader(fileDataPath)
        for data in dataReader.readData():
            customer = createCustomer(data)
            party.addGuest(customer)
        party.sortGuests('id', 'ASC')
        printPartyGuests(party)
    except Exception:
        print("Program has finished due an error.")

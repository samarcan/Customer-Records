from models import Customer, Location, Headquarter, Party
from utils.datareader import DataReader


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


if __name__ == '__main__':
    hqLocation = Location(53.339428, -6.257664)
    headquarter = Headquarter('Intercom Dublin', hqLocation)
    party = Party(headquarter, 100)
    dataReader = DataReader('./assets/customers.txt')
    for data in dataReader.readData():
        customer = createCustomer(data)
        party.addGuest(customer)
    party.sortGuests('id', 'ASC')
    printPartyGuests(party)

#Mengimport Kelas Vehicle
from Vehicle import Vehicle

class Ship(Vehicle):
    #Constructor
    def __init__(self, countryOfManufacture = "", length = 0, beam = 0):
        self.__countryOfManufacture = countryOfManufacture
        self.__length = length
        self.__beam = beam
        
    #Setter Getter
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    def setLength(self, length):
        self.__length = length
    
    def setBeam(self, beam):
        self.__beam = beam
    
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    def getLength(self):
        return self.__length
    
    def getBeam(self):
        return self.__beam
    
    #Method
    #Show Ship Class
    def printShipClass(self):
        print("---------------------")
        print("Ship Name                : " + self.getModelName())
        print("Ship Type                : " + self.getType())
        print("Country of Manufacture   : " + self.__countryOfManufacture)
        print("Fuel Type                : " + self.getFuelType())
        print("Length                   : " + str(self.__length))
        print("Beam                     : " + str(self.__beam))
        print("Max Passengers           : " + str(self.getMaxPassengers()))
        print("Age                      : " + str(self.getAge()))
        self.Move()
        print("---------------------")
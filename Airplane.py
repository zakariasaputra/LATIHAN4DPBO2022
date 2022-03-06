#Mengimport Kelas Vehicle
from Vehicle import Vehicle

class Airplane(Vehicle):
    #Constructor
    def __init__(self, wingsLength = 0, firstFlight = 0, status = ""):
        self.__wingsLength = wingsLength
        self.__firstFlight = firstFlight
        self.__status = status
        
    #Setter Getter
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def setFirstFlight(self, firstFlight):
        self.__firstFlight = firstFlight
    
    def setStatus(self, status):
        self.__status = status
    
    def getWingsLength(self):
        return self.__wingsLength
    
    def getFirstFlight(self):
        return self.__firstFlight

    def getStatus(self):
        return self.__status
    
    #Method
    #Show Airplane Class
    def printAirplaneClass(self):
        print("---------------------")
        print("Airplane Name            : " + self.getModelName())
        print("Aiplane Type             : " + self.getType())
        print("First Flight             : " + str(self.__firstFlight))
        print("Fuel Type                : " + self.getFuelType())
        print("Wings Length             : " + str(self.__wingsLength))
        print("Max Passengers           : " + str(self.getMaxPassengers()))
        print("Age                      : " + str(self.getAge()))
        print("Status                   : " + self.__status)
        self.Move()
        print("---------------------")
class Vehicle:
    #Constructor
    def __init__(self, modelName = "", fuelType = "", maxPassenger = 0, age = 0, tipe = ""):
        self.__modelName = modelName
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassenger
        self.__age = age
        self.__type = tipe
        
    #Setter Getter
    def setModelName(self, modelName):
        self.__modelName = modelName
    
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
    
    def setAge(self, age):
        self.__age = age
    
    def setType(self, tipe):
        self.__type = tipe
    
    def getModelName(self):
        return self.__modelName

    def getFuelType(self):
        return self.__fuelType
    
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    def getAge(self):
        return self.__age
    
    def getType(self):
        return self.__type
    
    #Move Method 
    def Move(self):
        print(self.__modelName + " is moving.")
    
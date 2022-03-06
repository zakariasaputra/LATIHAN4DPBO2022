#Mengimport Kelas Driver
from Driver import Driver

class Person:
    #Constructor
    def __init__(self, nik = "", name = "", gender = "", driver = Driver()):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
        self.__driver = driver
    
    #Setter Getter
    def setNik(self, nik):
        self.__nik = nik
    
    def setName(self, name):
        self.__name = name
    
    def setGender(self, gender):
        self.__gender = gender

    def setDriver(self, driver):
        self.__driver = driver
    
    def getNik(self):
        return self.__nik
    
    def getName(self):
        return self.__name
    
    def getGender(self):
        return self.__gender
    
    def getDriver(self):
        return self.__driver
    
    #Sleep Method
    def Sleep(self):
        print(self.__name + " keur sare.")
    
    #Method
    #Show Person Class
    def printtPersonClass(self):
        print("---------------------")
        print("NIK              : " + self.__nik)
        print("Name             : " + self.__name)
        print("Gender           : " + self.__gender)
        print("Driver License   : " + self.__driver.getLicenseId())
        print("Active Until     : " + str(self.__driver.getActiveUntil()))
        print("Vehicle Type     : " + self.__driver.getVehicleType())
        print("NIP              : " + self.__driver.getNip())
        print("Company Name     : " + self.__driver.getCompanyName())
        print("Position         : " + self.__driver.getPosition())
        self.Sleep()
        print("---------------------")
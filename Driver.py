#Mengimport Kelas Job
from Job import Job

class Driver(Job):
    #Constructor
    def __init__(self, licenseId = "", activeUntil = 0, vehicleType = ""):
        self.__licenseId = licenseId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    #Setter Getter
    def setLicenseId(self, licenseId):
        self.__licenseId = licenseId
    
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    
    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getLicenseId(self):
        return self.__licenseId
    
    def getActiveUntil(self):
        return self.__activeUntil
    
    def getVehicleType(self):
        return self.__vehicleType
    
    

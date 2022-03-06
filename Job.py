class Job:
    #Constructor
    def __init__(self, nip = "", companyName = "", position = ""):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position
    
    #Setter Getter
    def setNip(self, nip):
        self.__nip = nip
    
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    
    def setPosition(self, position):
        self.__position = position
    
    def getNip(self):
        return self.__nip
    
    def getCompanyName(self):
        return self.__companyName
    
    def getPosition(self):
        return self.__position
    
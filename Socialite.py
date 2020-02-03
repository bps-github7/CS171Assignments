##Ben Sehnert---bps53@drexel.edu---12455911
##CS172
##Professor D. Augenblick

##HW1 socialite class
class Socialite:

    #initializer method
    def __init__(self):
        self.__lastName = ''
        self.__firstName = ''
        self.__picture = ''
        self.__website = ''
        self.__description = ''
        self.__userID = ''
    
    #Mutator Methods
    def setLastName(self, lastName):
        self.__lastName = lastName
        
    def setFirstName(self, firstName):
        self.__firstName = firstName
    
    def setPicture(self, picture):
        self.__picture = picture
    
    def setWebsite(self, website):
        self.__website = website
    
    def setDescription(self, description):
        self.__description = description
    
    def setUserID(self, userID):
        self.__userID = userID

    #Accessor Methods
    def getLastName(self):
        return self.__lastName
    
    def getFirstName(self):
        return self._firstName
    
    def getPicture(self):
        return self._picture

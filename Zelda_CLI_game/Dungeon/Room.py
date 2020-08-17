##Ben Sehnert
##8-8-18
##CS172 room class

class Room:
	#Constructor sets the description
	#All four doors should be set to None to start
	def __init__(self,descr):
		#Description of the room to print out
		#These should be unique so the player knows where they are
		self.__descr = descr
		#These either tell us what room we get to if we go through the door
		#or they are None if the "door" can't be taken.
		self.__north = self
		self.__south = self
		self.__east = self
		self.__west = self
	#Access
	#Return the correct values
	def __str__(self):
            return self.__descr
	def getNorth(self):
	    return self.__north
	def getSouth(self):
            return self.__south
        def getEast(self):
	    return self.__east
	def getWest(self):
	    return self.__west
	#Mutators
	#Update the values
	def setDescription(self,d):
	    self.descr = d;
	def setNorth(self,n):
		self.__north = n
	def setSouth(self,s):
		self.south = s
	def setEast(self,e):
		self.east = e
	def setWest(self,w):
		self.west = w
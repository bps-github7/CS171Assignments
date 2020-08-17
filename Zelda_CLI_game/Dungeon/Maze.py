class Maze:
	#Inputs: Pointer to start room and exit room
	#Sets current to be start room
	def __init__(self,st=None,ex=None):
		#Room the player starts in
		self.__start_room = st
		#If the player finds this room they win
		self.__exit_room = ex
		#What room is the player currently in
		self.__current = st
	#Return the room the player is in (current)
	def getCurrent(self):
            return self.__current
	#The next four all have the same idea
	#See if there is a room in the direction
	#If the direction is None, then it is impossible to go that way
	#in this case return false
	#If the direction is not None, then it is possible to go this way
	#Update current to the new move (move the player)
	#then return true so the main program knows it worked.
	def moveNorth(self):
            if (self.__current == self.__current.getnorth()):
                return false
            else:
                return True
	def moveSouth(self):
	    if (self.__current == self.__current.getsouth()):
                return false
            else:
                return True
	def moveEast(self):
            if (self.__current == self.__current.geteast()):
                return false
            else:
                return True
	def moveWest(self):
            if (self.__current == self.__current.getsouth()):
                return false
            else:
                return True
	#If the current room is the exit,
	#then the player won! return true
	#otherwise return false
	def atExit(self):
		self.current = self.exit_room
	#If you get stuck in the maze, you should be able to go
	#back to the start
	#This sets current to be the start_room
	def reset(self):
            self.__current = self.__start_room;
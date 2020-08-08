##Ben Sehnert
##8/29/2018
##CS172-HW4
##drawable Abstract Base Class

import abc;#import statement

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self,x=0,y=0,color=(0,0,255)):#class constructor
        self.__x=x;
        self.__y=y;
        self.__color=color;
    
    def getcolor(self):#accessor method for color
        return self.__color;
    
    def getX(self):#accessor methods for x coordinate
        return self.__x;
    
    def getY(self):#accessor method for y coordinate
        return self.__y;
    
    def getLoc(self):#accessor method for the x,y coordinate pair
        return self.getX(),self.getY()

    def setLoc(self,p):#mutator method
        self.__x = p[0];
        self.__y = p[1];
        
    @abc.abstractmethod
    def draw(self,surface):
        pass;
    
    @abc.abstractmethod
    def getRect(self,surface):
        pass;

if __name__ == "__main__":
    print("Running in standby mode.");#notifies the user that class is being ran rather then actual program
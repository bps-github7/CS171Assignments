import pygame
from Drawable import *

class Ball(Drawable):#class constructor uses x,y w for the coordinates and width, color defaults to red
     def __init__(self,x,y,r,w,color=(0,0,255)):
          super().__init__(x,y)
          self.__r = r
          self.__w = w
          self.__color = color        
    
     def getW(self):#accessor method for width
          return self.__w

     def draw(self,surface):
          pygame.draw.circle(surface,(0,0,0),self.getLoc(),self.__r,5)
          pygame.draw.circle(surface,(255,0,0),self.getLoc(),self.__r)
    
     def getRect(self,surface):
          loc = self.getLoc()
          return pygame.Rect([loc[0]-12,loc[1]-20,30,30])
        
     def bounce(self, diff):
          """ 
     This function will bounce the ball
     off a horizontal surface (not a vertical one)
          """
          self.direction = (180 - self.direction) % 360
          self.direction -= diff

     def update(self):
          """ Update the position of the ball. """
          # Sine and Cosine work in degrees, so we have to convert them
          direction_radians = math.radians(self.direction)
 
          # Change the position (x and y) according to the speed and direction
          self.x += self.speed * math.sin(direction_radians)
          self.y -= self.speed * math.cos(direction_radians)
 
          # Move the image to where our x and y are
          self.rect.x = self.x
          self.rect.y = self.y
 
          # Do we bounce off the top of the screen?
          if self.y <= 0:
               self.bounce(0)
               self.y = 1
 
          # Do we bounce off the left of the screen?
          if self.x <= 0:
               self.direction = (360 - self.direction) % 360
               self.x = 1
 
          # Do we bounce of the right side of the screen?
          if self.x > self.screenwidth - self.width:
               self.direction = (360 - self.direction) % 360
               self.x = self.screenwidth - self.width - 1
 
          # Did we fall off the bottom edge of the screen?
          if self.y > 600:
               return True
          else:
               return False

     

if __name__ == "__main__":
    print("running in standby mode")
    pygame.init()
    surface = pygame.display.set_mode((400,300))
    
    #creates drawable container
    drawables = []

    while(True):
	#escape sequence
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                pos = event.__dict__['pos']
                drawables.append(Ball(pos[0],pos[1],8,4))
        
        #surface created
        surface.fill((255,255,255))
        for drawable in drawables:
            drawable.draw(surface)
        
        #updates the surface
        pygame.display.update()
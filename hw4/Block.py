import pygame
from Drawable import *

class Block(Drawable):
    def __init__(self,x,y,w=20, visible=True, color=(255,255,255)):
        '''
    class constructor uses x,y w for the coordinates and width, color defaults to red
        '''
        super().__init__(x,y)
        self.__w = w
        self.__visible = True
        self.__color = color
    
    def getW(self):
        return self.__w
    
    def setVis(self):
        self.__visible = False
    
    def draw(self, surface, collision):
        if not collision:
            pygame.draw.rect(surface, (0,0,0), (super().getX() - self.getW() / 2, super().getY() - self.getW() / 2, self.getW(), self.getW()),4)
            pygame.draw.rect(surface, (0,0,255), (super().getX() - self.getW() / 2, super().getY() - self.getW() / 2, self.getW(), self.getW()))
        else:
            pass
        
    def getRect(self,surface):
        loc = self.getLoc()
        return pygame.Rect([loc[0]-15,loc[1]-20,30,30])
        

if __name__ == "__main__":
    print("running in standby mode")
    pygame.init()
    surface = pygame.display.set_mode((400,300))
    
    #initialize list drawable
    drawables = []
    
    while (True): #unit testing for the square class
	
	#escape sequence
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                pos = event.__dict__['pos']
                drawables.append(Block(pos[0],pos[1]))
    
        #surface created
        surface.fill((255,255,255))
        for drawable in drawables:
            drawable.draw(surface)
        
        #updates the surface
        pygame.display.update()

import pygame;
from Drawable import *

class Text(Drawable):
    def __init__(self, x, y, message, color =(0,0,0)):
        super().__init__(x,y)
        fontObj = pygame.font.Font('freesansbold.ttf',32)
        self.surface = fontObj.render(message, True, color)

    def draw(self,surface):
        surface.blit(self.surface,self.getLoc())
    
    def getRect(self,surface):
        pass;

if __name__ == "__main__":
    #print("running in standby mode");
    pygame.init()
    surface = pygame.display.set_mode((400,300))
    
    #initialize list drawable
    test = Text(10,20,"test")
    
    while True: #unit testing for the square class
	
	#escape sequence
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
    
        #surface created
        surface.fill((255,255,255))
        test.draw(surface)
        
        
        #updates the surface
        pygame.display.update()
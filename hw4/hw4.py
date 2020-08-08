###Ben Sehnert
###8/31/2018
###CS172 HW4

#import statements
import time
import pygame
from Ball import *
from Block import *
from Text import *

#so much of this code could be better organizaed. 
# bet u get it working after everything straightened out



#Pygame initialized, fps & surface objects created

pygame.init()
fps = pygame.time.Clock()
surface = pygame.display.set_mode((500,500))

# pygame_init()

#global declaration for ball, xv and yv object
global ball
ball = Ball(20,393,8,7)
global xv
global yv
#dont use global variables


def intersection(rect1,rect2):
    '''Detects collisions, takes two getRect() rectengles as objects'''
    x1,y1,w1,h1 = rect1
    x2,y2,w2,h2 = rect2
    print(x2)
    if x1 >= x2:
        return True
    elif x1 + w1 >= x2:
        return True
    elif y1 >= y2 + h2:
        return True
    elif h1 + y1 <= y2:
        return True
    else:
        return False

def blockCheck(blocks,ball):
    '''makes blocks turn invisible when struck by ball'''
    for block in blocks:
        if intersection(ball.getRect(surface),block.getRect(surface)):
            collision == True
            return collision

def moveBall(xv,yv):
    '''handles ball physics. takes x and y velocity, moves ball along parabolic path using setLoc and draw method. no return values.'''
    dt = 0.1
    g = 10
    r = 0.7
    eta = 0.5
    if ball.getY() > 400:
        ball.setLoc((ball.getX(),389))
        yv = -r  * yv
        xv = eta * xv
    elif xv and yv < 0:
        ball.setLoc((ball.getX(),ball.getY()))
    elif xv != 0 or yv != 0:
        ball.setLoc((ball.getX()+int(dt*xv),(ball.getY()-int(dt*yv))))
    else:
        yv = yv - g * dt

def blockStacker(x,y,collision):
    '''draws a single block in intended position. takes the number of x,y coodinates nessc for blocks to be stacked 3x3.'''
    block = Block(400 + x,389 + y)
    block.draw(surface,collision)
    blocks.append(block)

def row(y,collision):
    '''draws a single row of blocks'''
    for x in range(0,60,20):
        blockStacker(x,y,collision)

collision = False
xv = 0
yv = 0
while(True):#game loop intializes here
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            mx_d, my_d = pygame.mouse.get_pos()
        elif (event.type == pygame.MOUSEBUTTONUP):
            mx_u, my_u = pygame.mouse.get_pos()
            #initial x velocity
            xv = mx_u - mx_d
            #initial y velocity
            yv = -1*(my_u - my_d)
    surface.fill((255,255,255))
    #initializes a list for blocks
    blocks = []
    #intializes the
    ball.draw(surface)
    moveBall(xv,yv)
    #draws line to represent ground
    ground = pygame.draw.line(surface,(0,0,0),(0,400),(500,400))
    #creates text item and appends to drawable
    score = 0
    message = Text(10,10,"score: {}".format(score),(0,0,0))
    message.draw(surface)
    #calls blockStacker() function with list containing increments for the adusted block coords
    row(0,collision)
    row(-20,collision)
    row(-40,collision)
    #calls block check function
    collision = blockCheck(blocks,ball)
    #tick method and updates display
    fps.tick(60)
    pygame.display.update()
#if __name__ == '__main__':
##    main()
##    pygame.quit()
##    sys.exit()
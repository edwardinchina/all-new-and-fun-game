import pygame
from pygame import Rect
from pygame import draw
from pygame import Vector2


WIDTH = 1080
HEIGHT = 720
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS


class Node:
    
    def __init__(self,color,loc,size):
        self.color = color
        self.loc = Vector2(loc)
        self.size = Vector2(size)
        self.rect = Rect(loc,size)
        self.left = None
        self.right = None

    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)
        if(self.left):
            self.left.draw()
        if(self.right):
            self.right.draw()

    def append_left(self, color):
        UPLEFT = Vector2(-self.size.x,-self.size.y)
        self.left = Node(color,self.loc+UPLEFT,self.size)

    def append_right(self, color):
        UPRIGHT = Vector2(self.size.x,-self.size.y)
        self.right = Node(color,self.loc+UPRIGHT,self.size)


root = Node(WHITE,(500,500),(50,50))
# root.left = Node(GREEN,(450,400),(40,40))
root.append_left(GREEN)

# root.right = Node(RED,(550,400),(40,40))
root.append_right(RED)



root.left.append_left(GREEN)
root.left.append_right(RED)

root.right.append_left(GREEN)
root.right.append_right(RED)


root.right.right.append_right(RED)


root.right.right.right.append_right(RED)


root.draw()


pygame.display.flip()       

running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

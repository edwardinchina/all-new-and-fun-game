import pygame
import os

def angle_of_vector(x, y):
    return math.Vector2(x, y).angle_to((1, 0))  # 2: with pygame.math.Vector2.angle_to
    
def angle_of_line(x1, y1, x2, y2):
    return angle_of_vector(x2-x1, y2-y1)               # 2: pygame.math.Vector2.angle_to

# Start the game
pygame.init()
game_width = 1500  
game_height = 700
screen = pygame.display.set_mode((game_width, game_height))
running = True

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blit(self, pic, p):
        x,y = p
        screen.blit(pic, ((x -self.x) -150, (y -self.y)- 150))

    # def rect(self, rect, color):
    #     rect = rect.                # move rectangle before drawing.
    #     pygame.draw.rect(screen, color, rect)

mouse_x = 0
mouse_y = 0
cam = Camera(0,0)


size = 10
player = pygame.Rect( (game_width - size) / 2, (game_height-size) /2, size, size)


class Snake:
    def __init__(self,x,y,follow_part, isHead, number):
        self.x = x
        self.y = y
        self.dir =0
        self.speed = (1 - number / 10)/2
        #if isHead:
            #self.speed = 0.2
        #else:
            #self.speed = 0.1
        self.hitbox = pygame.Rect(0, 0, 150, 150)
        self.pic = pygame.image.load("tremmer\Tremor Scales.png")
        self.pic_small = pygame.transform.scale(self.pic, (150,150))
        self.pic_small.set_colorkey((255,255,255))
        self.pic_small = pygame.Surface.convert_alpha(self.pic_small)
        self.follow_part = follow_part
        self.isHead = isHead

    def draw(self):
        tempicp = pygame.transform.rotate(self.pic_small, self.dir)
        cam.blit(tempicp , (self.x , self.y))


    def update (self):
        if self.isHead:
            follow_x = player_x + 5
            follow_y = player_y + 5
        else:
            follow_x = self.follow_part.x - 75
            follow_y = self.follow_part.y - 75

        # use the function below:
        angle_of_line(__,__,__,__)
        
        pygame.draw.line(screen, (255,255,255),pos,pos2,2)
        print(self.dir) 

   
        if self.x - 75 > follow_x:
            self.x += -self.speed
            
        if self.x - 75 < follow_x:
            self.x += self.speed
                
        if self.y - 75 < follow_y:
            self.y += self.speed
                
        if self.y - 75 > follow_y:
            self.y += -self.speed

    

    def distance(self):
        f_x = self.follow_part.x
        f_y = self.follow_part.y
        self.d = math.sqrt( self.x**2 + self.y**2 )





snake = []

follow_part = None
for i in range (0,5):
    new_part = Snake(300,300 + i *100,follow_part, i == 0,i)
    snake.append(new_part)
    follow_part = new_part
    
speed = 1.5
player_x = player.x
player_y = player.y



# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((102, 51, 0))
    pygame.draw.rect(screen,(255,255,255),player)
    for s in snake:
        s.update()
    for s in snake:
        s.draw()


    
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()


        if game_width / 2 > mouse_x - size /2:
            cam.x += -speed
            player_x += -speed
                    
        if game_width / 2 < mouse_x - size /2:
            cam.x += speed
            player_x += speed
                    
        if game_height /2 < mouse_y - size /2:
            cam.y += speed
            player_y += speed
                    
        if game_height /2 > mouse_y - size /2:
            cam.y += -speed
            player_y += -speed


    # Tell pygame to update the screen
    pygame.display.update()
    # print(cam.x)
    # print(player.x)
    # print(snake[0].x)


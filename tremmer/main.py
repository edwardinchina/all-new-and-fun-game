import pygame
import pygame.math as math
import os


def angle_of_vector(x, y):
    return math.Vector2(x, y).angle_to((1, 0))  # 2: with pygame.math.Vector2.angle_to


def angle_of_line(x1, y1, x2, y2):
    return angle_of_vector(x2-x1, y2-y1)               # 2: pygame.math.Vector2.angle_to


def spring_force(x1, y1, x2, y2, k, d):
    diff = math.Vector2(x2,y2) - math.Vector2(x1,y1)
    if diff == math.Vector2(0,0):
        diff = math.Vector2(d,0)
    else:
        diff = diff - diff.normalize()*d
    return diff*k


# Start the game
pygame.init()
game_width = 1500  
game_height = 700
screen = pygame.display.set_mode((game_width, game_height))
running = True

class Node:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_vector2(self):
        return math.Vector2(self.x, self.y)


class Camera(Node):
    def blit(self, pic, p):
        x,y = p
        screen.blit(pic, ((x -self.x) -150, (y -self.y)- 150))

    def line(self, color, pos1, pos2, width):
        x1, y1 = pos1
        x2, y2 = pos2
        pygame.draw.line(screen, color, (x1-self.x,y1-self.y), (x2-self.x,y2-self.y), width)

    def rect(self, color, rect, width=0):
        rect = rect.move(-self.x, -self.y)
        pygame.draw.rect(screen, color, rect, width)

    def get_mouse_vector(self,mouse_screen):
        return mouse_screen + self.get_vector2()

class FollowCamera(Camera):
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target

    def update(self):
        dx, dy = spring_force(self.x+game_width/2, self.y+game_height/2, self.target.x, self.target.y, .001, 50)
        self.x += dx
        self.y += dy


class Player(Node):
    '''Player on client
    '''
    def __init__(self, x, y, box):
        '''

        Args:
            box ([type]): [description]
            x (float, optional): mid. Defaults to 0.
            y (float, optional): mid. Defaults to 0.
        '''
        super().__init__(x,y)
        self.box = box

    def get_rect(self):
        return self.box.move(self.x, self.y)



class Snake:
    def __init__(self, x, y, follow_part, isHead, number):
        self.x = x
        self.y = y
        self.dir = 0
        self.speed = (1 - number / 10)/2
        self.hitbox = pygame.Rect(0, 0, 150, 150)
        if isHead:
            self.pic = pygame.image.load("tremmer\\untitled.png")
        else:
            self.pic = pygame.image.load("tremmer\Tremor Scales.png")
        self.pic_small = pygame.transform.scale(self.pic, (150,150))
        self.pic_small.set_colorkey((255,255,255))
        self.pic_small = pygame.Surface.convert_alpha(self.pic_small)
        self.follow_part = follow_part
        self.isHead = isHead

    def draw(self):
        tempicp = pygame.transform.rotate(self.pic_small, self.dir)
        cam.blit(tempicp, (self.x, self.y))


        if self.isHead:
            follow_x = player.x + 5
            follow_y = player.y + 5
        else:
            follow_x = self.follow_part.x
            follow_y = self.follow_part.y

        cam.line((255,255,255), (self.x,self.y), (follow_x,follow_y), 4)

    def update(self):
        if self.isHead:
            follow_x = player.x + 5
            follow_y = player.y + 5
        else:
            follow_x = self.follow_part.x
            follow_y = self.follow_part.y

        # use the function below:
        self.dir = angle_of_line(self.x, self.y, follow_x, follow_y) - 90
        
        # pygame.draw.line(screen, (255,255,255),pos,pos2,2)

        dx,dy = spring_force(self.x,self.y,follow_x,follow_y,0.3,50)
        self.x += dx
        self.y += dy

    def distance(self):
        f_x = self.follow_part.x
        f_y = self.follow_part.y
        self.d = math.sqrt(self.x**2 + self.y**2)


class Tile(pygame.Rect):
    def __init__(self, x, y, w, h):
        super().__init__(x,y,w,h)

    def draw(self):
        cam.rect((0,0,0),self,5)
        cam.rect((95,80,15),self)


tiles = []
tile_width = game_width/10
tile_height = game_height/10
for i in range(0,10):
    row = []
    for j in range(5,10):
        row.append(Tile(i*tile_width, j*tile_height, tile_width, tile_height))
    tiles.append(row)


size = 10
player = Player(game_width/2, game_height/2, pygame.Rect(-size/2, -size/2, size, size))

snake = []

follow_part = None
for i in range(0, 5):
    new_part = Snake(300, 300 + i * 100, follow_part, i == 0, i)
    snake.append(new_part)
    follow_part = new_part
 
speed = 1.5

mouse_x = 0
mouse_y = 0
cam = FollowCamera(0, 0, player)


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
    cam.rect((255,255,255), player.get_rect())

    ## Update phyics
    for s in snake:
        s.update()
    if pygame.mouse.get_pressed()[0]:
        mouse_screen = math.Vector2(pygame.mouse.get_pos())
        mouse_vector = cam.get_mouse_vector(mouse_screen)

        direction = (mouse_vector - player.get_vector2()).normalize()
        
        player.x += direction.x * speed
        player.y += direction.y * speed

    ## Draw
    cam.update()
    for s in snake:
        s.draw()
    for row in tiles:
        for t in row:
            t.draw()

    # Tell pygame to update the screen
    pygame.display.update()
    # print(cam.x)
    # print(player.x)
    # print(snake[0].x)


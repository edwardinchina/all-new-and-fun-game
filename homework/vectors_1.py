import pygame
import math

pygame.init()
game_width = 1000
game_height = 700
screen = pygame.display.set_mode((game_width, game_height))


class Bullet:
    def __init__(self,s,v):
        self.x = s.x
        self.y = s.y
        self.v = v
        self.hitbox = pygame.Rect(self.x, self.y, 10, 10)

    def update(self):
        self.x += self.v.x
        self.y += self.v.y
        self.hitbox = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox)


bullets = []
running = True
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((0,0,0))


    mx,my = pygame.mouse.get_pos()
    m = pygame.math.Vector2(mx,my)
    c = pygame.math.Vector2(game_width /2 ,game_height /2)
    v = m-c
    vn = v.normalize()
    vn2 = v.normalize() *60 + c
    #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    bullets.append(Bullet(vn2,vn))
    for b in bullets:
        b.update()
    pygame.draw.line(screen, (255,255,255), (c), (vn2), 10)
    pygame.display.update()
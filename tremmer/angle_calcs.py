import pygame
import pygame.math as math

def angle_of_vector(x, y):
    return math.Vector2(x, y).angle_to((1, 0))  # 2: with pygame.math.Vector2.angle_to
    
def angle_of_line(x1, y1, x2, y2):
    return angle_of_vector(x2-x1, y2-y1)               # 2: pygame.math.Vector2.angle_to
    
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

angle = 0
radius = 150
vec = math.Vector2(radius, 0)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    cpt = window.get_rect().center
    pt = cpt[0] + vec[0], cpt[1] + vec[1]
    angle = angle_of_vector(*vec)

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), cpt, radius, 1)
    pygame.draw.line(window, (0, 255, 0), cpt, (cpt[0] + radius, cpt[1]), 3)
    pygame.draw.line(window, (255, 0, 0), cpt, pt, 3)
    text_surf = font.render(str(round(angle/5)*5) + "°", True, (255, 0, 0))
    text_surf.set_alpha(127)
    window.blit(text_surf, text_surf.get_rect(bottomleft = (cpt[0]+20, cpt[1]-20)))
    pygame.display.flip()

    vec = vec.rotate(1)

pygame.quit()
exit()

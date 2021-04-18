import pygame
import pygame.math as math

mid = math.Vector2(0,0)
top_right = math.Vector2(1,1)
right = math.Vector2(5,1)
Diff = top_right - right
print(mid.x)
print(mid.y)
print(Diff)

# Length of Diff
print(Diff.length())

# Distance from right to top_right
print(right.distance_to(top_right))

print(right.angle_to(top_right))

print(mid.angle_to(top_right))

print(math.Vector2.angle_to(Diff))

import pygame
import math








'''
Coding Assignment: write code using math.Vector2 and vec.normalize() to print out the normalized form of these vectors. (keep code that prints all 5 answers) 
a. (1,0) (Answer is (1,0) ) b. (5,0) c. (-5,0) d. (1,1) e. (5,5)
'''

# a (1,0)
vec = pygame.math.Vector2(1,0)

print(str(vec.normalize()) + " " + str(vec.length()))


# b: answer: ()

vec = pygame.math.Vector2(5,0)

print(str(vec.normalize()) + " " + str(vec.length()))

# c
vec = pygame.math.Vector2(-5,0)
print(str(vec.normalize()) + " " + str(vec.length()))

# d answer:  len = sqrt(2)
vec = pygame.math.Vector2(1,1)
print(str(vec.normalize()) + " " + str(vec.length()))


# e
vec = pygame.math.Vector2(5,5)
print(str(vec.normalize()) + " " + str(vec.length()))


# bonus
vec = pygame.math.Vector2(3,4)
print(str(vec.normalize()) + " " + str(vec.length()))
vec = pygame.math.Vector2(4,3)
print(str(vec.normalize()) + " " + str(vec.length()))



vec = pygame.math.Vector2(0.6,0.8)
print(str(vec.normalize()) + " " + str(vec.length()))
"""
Simple aleatory collor with python.
Test the program changing the numbers...

Createad by - Gabriel Melo, Brazil
"""
import random
import pygame
from pygame.locals import*
from sys import exit

pygame.init()

width = 640
height = 480
x = 320
y = 240

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((width, height))

pygame.display.set_caption('Aleatory Paint')

while True:


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        
        if event.type == KEYDOWN:
            if event.key == K_h:
                tela.fill((12, 6, 9))
    

    x -= random.randint(6, 21)

    x += random.randint(6, 21)

    y -= random.randint(6, 21)
    
    y += random.randint(6, 21)

    
    # A condition event, X for Widht and Y for Height
    #  For object don't pass the board.
    if x >= 641:
        x = 1
    if x <= 0:
        x = 640
    if y >= 641:
        y = 1
    if y <= 0:
        y = 640
    
    # Aleatory collor i used module random.
    red = random.randint(1, 200)
    green = random.randint(1, 200)
    blue = random.randint(1, 200)

    pygame.draw.rect(tela, (red, green, blue), (x, y, 10, 20))

    pygame.display.update()

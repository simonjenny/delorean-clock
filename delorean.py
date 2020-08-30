#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ["SDL_FBDEV"] = "/dev/fb1"

import pygame, random
from datetime import datetime

pygame.init()

BLACK  = (0, 0, 0)

X = 800
Y = 480

def alter():
    while True:
        yield 0
        yield 7

alt = alter()

screen = pygame.display.set_mode((X, Y))

def Print(str, location, color, alpha):

    font = pygame.font.Font('lcd.ttf', 50)
    text = font.render(str, True, color)
    text.set_alpha(alpha)
    text_rect = text.get_rect(center=location)
    screen.blit(text, text_rect)

    m = "8" if str.isdigit() else "O"
    font = pygame.font.Font('lcd.ttf', 50)
    shadow = font.render(m * len(str), True, (255,255,255))
    shadow.set_alpha(50)
    shadow_rect = shadow.get_rect(center=location)
    screen.blit(shadow, shadow_rect)

def Circle(location, color, radius):
    pygame.draw.circle(screen, color, location, radius)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

screen.fill(BLACK)
BackGround = Background('bg.png', [0,0])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    screen.blit(BackGround.image, BackGround.rect)

    now = datetime.now()
    #Destination
    ORANGE = (215,97,47)
    ALPHA1 = random.randint(235, 255)
    Print(now.strftime("%b").upper(), (80, 80), ORANGE, ALPHA1) #MONTH
    Print(now.strftime("%d"), (227, 80), ORANGE, ALPHA1) #DAY
    Print(now.strftime("1955"), (380, 80), ORANGE, ALPHA1) #YEAR
    Print(now.strftime("%H"), (608, 80), ORANGE, ALPHA1) #HOUR
    Print(now.strftime("%M"), (736, 80), ORANGE, ALPHA1) #MINUTR

    #Pesent
    GREEN  = (141,194,90)
    ALPHA2 = random.randint(235, 255)
    Print(now.strftime("%b").upper(), (80, 240), GREEN, ALPHA2) #MONTH
    Print(now.strftime("%d"), (227, 240), GREEN, ALPHA2) #DAY
    Print(now.strftime("%Y"), (380, 240), GREEN, ALPHA2) #YEAR
    Print(now.strftime("%H"), (608, 240), GREEN, ALPHA2) #HOUR
    Print(now.strftime("%M"), (736, 240), GREEN, ALPHA2) #MINUTR

    #Last
    YELLOW = (255,223,126)
    ALPHA3 = random.randint(235, 255)
    Print(now.strftime("%b").upper(), (80, 403), YELLOW, ALPHA3) #MONTH
    Print(now.strftime("%d"), (227, 403), YELLOW, ALPHA3) #DAY
    Print(now.strftime("1985"), (380, 403), YELLOW, ALPHA3) #YEAR
    Print(now.strftime("%H"), (608, 403), YELLOW, ALPHA3) #HOUR
    Print(now.strftime("%M"), (736, 403), YELLOW, ALPHA3) #MINUTR

    RADIUS = alt.next()

    Circle((668, 65), ORANGE, RADIUS)
    Circle((668, 87), ORANGE, RADIUS)

    Circle((668, 224), GREEN, RADIUS)
    Circle((668, 246), GREEN, RADIUS)

    Circle((668, 390), YELLOW, RADIUS)
    Circle((668, 412), YELLOW, RADIUS)

    if now.strftime('%p') == "am":
        Circle((503, 44), ORANGE, 7)
        Circle((503, 204), GREEN, 7)
        Circle((503, 370), YELLOW, 7)
    else:
        Circle((503, 88), ORANGE, 7)
        Circle((503, 248), GREEN, 7)
        Circle((503, 414), YELLOW, 7)

    pygame.time.wait(1000)
    pygame.display.flip()

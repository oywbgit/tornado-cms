#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'
__mail__ = 'iishappyabu@163.com'


import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

# 可以用pygame.font.get_fonts()方法来获得当前系统所有可用字体
# print(pygame.font.get_fonts())
font = pygame.font.SysFont("", 40)
text_surface = font.render("Hello", True, (0, 0, 255))

x = 0
y = (480 - text_surface.get_height()) / 2

background = pygame.image.load("D:\\Mine\\Picture\\1538969268852_k9s4-0.jpg").convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 0.05
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))

    pygame.display.update()

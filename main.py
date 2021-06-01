import pygame
import time
import sys

from pygame_utilities import *
from ETS_main_pygame import *
from ETS_functions_pygame import *
from ETS_intro_pygame import * 
from ETS_rooms_pygame import *
from ETS_battles_pygame import *



first = True

while True:
 

    if first:
        header()
        text_slowmo("Thank you for playing", (200, Y//2), sleep = 1, font_size=30, speed=.05)
        text_wrap("Escaping Toro Sanctum", (200, 450), sleep = 1, fill = False, font_size=28)
        text_slowmo("Press 'P' to play again or 'Q' to quit", (200, 560), fill = False, speed = .04)
        first = False
    pygame.event.pump()

    for event in pygame.event.get():
 
    
        if event.type == pygame.QUIT:
 
  
            pygame.quit()

            quit()
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                escaping_sanctum(ETS_user)
            if event.key == pygame.K_q:
                pygame.quit()





        
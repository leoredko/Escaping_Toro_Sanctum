import pygame
import time
from pygame.locals import *

color_dict = {
"white" : (255, 255, 255),
"green" : (0, 255, 0),
"blue" : (0, 102, 204),
"black" : (0, 0, 0),
"red" : (255, 0, 0),
"yellow" : (255, 255, 0),
"cyan" : (0, 255, 255),
"magenta" : (255, 0, 255),
"orange" : (255, 128, 0) }

pygame.init()
X = 800
Y = 600


display_surface = pygame.display.set_mode((X, Y))



def write(text, location = (50, Y//2), color= "green", sleep = 0, font_size = 20, background = color_dict["black"]):
    font = pygame.font.SysFont('calibri', font_size)
    display_surface.fill(background)
    display_surface.blit(font.render(text,True,color_dict[color]),location)
    pygame.display.update()
    pygame.event.pump()
    time.sleep(sleep)
    pygame.event.pump()

def text_wrap(text, pos, surface=display_surface, font_size=20, color= "green", fill = True, box = False, sleep = 0):
    font = pygame.font.SysFont('calibri', font_size)
    if fill is True:
        surface.fill(color_dict["black"])
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0]  
    max_width, max_height = surface.get_size()
    x, y = pos
    num_rows = 1
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color_dict[color])
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                num_rows += 1
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space   
        x = pos[0]  
        y += word_height  
    if box:
        story_rect = pygame.Rect((pos[0]-2), (pos[1]-2), X-x, (num_rows*word_height+3)) 
        pygame.draw.rect(surface, color_dict["green"], story_rect, 1)    
    pygame.display.update()
    pygame.event.pump()
    time.sleep(sleep)
    





def text_slowmo(text, pos, color= "green", font_size=20, box = False, fill = True, sleep = 1, speed = .03):
    text += " "
    for i in range(1, len(text)):
        if text[i] == " ":
            text_wrap(text[0:i], pos, color=color, font_size = font_size, fill = fill, box = box)
        time.sleep(speed)
    time.sleep(sleep)



def ask(question, pos = (10, 200), fill = True, box = False, allow_empty = False):
    current_string = ""
    text_wrap(question, pos, fill = fill, box = box)
    while 1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                text_wrap(question + ": " + current_string, pos, color = "black",fill = fill, box = box)
                if event.key == pygame.K_BACKSPACE:
                    current_string = current_string[0:-1]
                elif event.key == pygame.K_RETURN:
                    if current_string != "" or allow_empty:
                        return current_string
                else:
                    if len(pygame.key.name(event.key)) == 1:
                        current_string += pygame.key.name(event.key)
                text_wrap(question + ": " + current_string, pos, fill = fill, box = box)


def pause():
    pausing = ask("press <enter> to continue...", (300, 570), fill = False, allow_empty = True)
    text_wrap("press <enter> to continue...", (300, 570), color = "black", fill = False)


def flash_text(text):
    write(text, sleep=.25)
    write(text, color = "black", background = "white", sleep =.25)
    write(text, sleep=.25)
    write(text, color = "black", background = "white", sleep =.25)
    write(text, sleep=.25)
    write(text, color = "black", background = "white", sleep = .25)
    write(text, sleep=2)

import sys
from pygame_utilities import *
import time
import random

slow = 2.5          
dia = 0.07
quick = 0.01
step = 1
from ETS_functions_pygame import *
from ETS_intro_pygame import * 
from ETS_rooms_pygame import *
from ETS_battles_pygame import *


time.sleep(step)

header()
time.sleep(step)
text_wrap("Escaping Toro Sanctum ® is a work of fiction. Characters, names, businesses, locations, \
events, and incidents are products of the authors and co-authors (you, the user) imagination. Any resemblance to actual persons, both \
living or dead, or actual events is purely coincidental ", (5, 180), fill = False)
time.sleep(slow)



class Player:
    def __init__(self, user_name, user_color, user_weight, user_item, bravo_leader, user_city, user_country):
        self.user_name = user_name
        self.user_color = user_color
        self.user_weight = user_weight
        self.user_item = user_item
        self.bravo_leader = bravo_leader
        self.user_city = user_city
        self.user_country = user_country
        self.hp = 100 
        self.dmg = 3

    def update_health(self,hp_change):
        self.hp = self.hp + hp_change


def get_user_input():
    write("Before we begin, we need to update your character profile", sleep = slow)
    user_name = (ask("What is your name, Team Leader?: >>> ").title())
    user_color = "red"
    user_weight = input_weight("In lbs, how much do you weigh?: >>> ")
    user_item = ask("Of the following, which item would you choose to carry with you? \n\
    [Select 1, 2, or 3 then press <enter> ]\n\n\
    1) A lucky coin\n\
    2) A golden locket\n\
    3) A bronze compass\n\n>>> ")
    if user_item == "1":
        user_item = "A lucky coin"
    elif user_item == "2":
        user_item = "A golden locket"
    elif user_item == "3":
        user_item = "A bronze compass"
    else:
        user_item = "empty"
    bravo_leader = "Lt. Macdonald"
    user_city = "Jekyll"
    user_country = "the United States"
    return(Player(user_name, user_color, user_weight, user_item, bravo_leader, user_city, user_country))

ETS_user = get_user_input()
text_slowmo(". . s a v i n g  d a t a . .", (250, Y//2), sleep = .75)
text_slowmo(". . s a v i n g  d a t a . .", (250, Y//2), sleep = .75)
text_slowmo(". . s a v i n g  d a t a . .", (250, Y//2), sleep = .75)
text_slowmo(". . s a v i n g  d a t a . .", (250, Y//2), sleep = .75)

starting_question(ETS_user)


introduction(ETS_user)


escaping_sanctum(ETS_user)

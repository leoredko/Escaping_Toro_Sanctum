import sys
import pygame
from ETS_functions_pygame import *
from pygame_utilities import *


class Zombie:
    def __init__(self):
        self.hp = 6
        self.dmg = 10
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def zombie_battle(ETS_user):
    zombie = Zombie()
    flash_text('A zombie is attacking you!')
    while zombie.hp > 0 and ETS_user.hp > 0:
        text_slowmo(f"Your current health is {ETS_user.hp}%", (300, 15))
        user_input = ask('Press A and then Enter to attack the zombie!\n>>> ', (10, 350), fill = False).lower()
        if user_input == 'a': 
            zombie.update_health(ETS_user.dmg * -1)
            write(f"You have shot and dealt {ETS_user.dmg} damage to the zombie", sleep = slow)
        if zombie.hp <= 0:
            break
        ETS_user.update_health(zombie.dmg * -1)
        text_slowmo(f"The zombie lunges at you and deals {zombie.dmg} damage !!", (5, 350), fill = False)
        
    
    if ETS_user.hp <= 0:
       write('You were killed by a Zombie, Game Over!', sleep = slow)
       sys.exit()
    else: 
        text_slowmo('You have defeated the zombie! ',(200, 300))
        
class Dead_team_member:
    def __init__(self):
        self.hp = 15
        self.dmg = 25
    def update_health(self,hp_change):
        self.hp = self.hp + hp_change

def Dead_team_member_battle(ETS_user):
    dead_team_member = Dead_team_member()
    text_slowmo("Up ahead is the silhouette of a Bravo Team member ... but something's wrong ...", (10, 280), sleep = 2, speed=.05)
    flash_text("A Dead Team Member is attacking you!")
    while dead_team_member.hp > 0 and ETS_user.hp > 0:
        text_slowmo(f"Your current health is {ETS_user.hp}%", (300, 15), speed=.05)
        user_input = ask('Press A and then Enter to attack the zombie team member!\n>>> ', (10, 350), fill = False).lower()
        if user_input == 'a': 
            dead_team_member.update_health(ETS_user.dmg * -1)
            write(f"You have shot and dealt {ETS_user.dmg} damage to the zombie team member", sleep = slow)
        ETS_user.update_health(dead_team_member.dmg * -1)
        text_slowmo(f"The zombie Bravo Team member lashes at you and deals {dead_team_member.dmg} damage!!", (10, 350), fill = False, speed=.05)
        
    
    if ETS_user.hp <= 0:
        write('You were killed by a dead team member', sleep = slow)
    else: 
        text_slowmo('You have defeated the dead team member!', (10, 300))
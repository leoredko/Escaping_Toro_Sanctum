from pygame_utilities import *
from ETS_functions_pygame import *
from ETS_battles_pygame import *
import sys
import random
import pygame
import time




wires_full = ["red", "blue", "yellow", "cyan", "magenta", "orange"]

boiler_keys_full = ["skull","blood","heart","spine"]

lever_direct = ["left", "right", "up", "down"]





def escaping_sanctum(ETS_user):
    ETS_user.hp = 100
    escaping_sanctum0 = ask("Will you search for Bravo Team and Escape Toro Sanctum? (Y/N)>>> ", (5, 300))
    if escaping_sanctum0 == "n" or escaping_sanctum0 == "N":
        text_slowmo("Understood ", (250, 400), fill = False)
        time.sleep(step)
        text_slowmo("Game Over ", (X//2, Y//2), color = "red")
        sys.exit()
    elif escaping_sanctum0 == "y" or escaping_sanctum0 == "Y":
        main_lobby(ETS_user)
    else:
        write("This isn\'t a valid response. Try again:\n", sleep = slow)
        escaping_sanctum(ETS_user)

def main_lobby(ETS_user):
    text_wrap("  Main Lobby ", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Alpha team continues onward, moving past the lobby. The polished linoleum floors reflect each movement. \
The dim emergency lights flicker, drawing the attention of the team. The rain becomes more faint as they reach the elevator and \
staircase section at the end of the lobby. The empty elevator shafts are hollowed silos extending in each direction. There is \
a sudden muffled sound that freezes {ETS_user.user_name} in their tracks ...", (5, 10), sleep = 2)
    zombie_battle(ETS_user)
    text_slowmo(f"Alpha team gathers around the body. As {ETS_user.user_name} kneels down to examine, the muffled sound becomes even louder ", (5, 10), sleep=2)
    pause()
    text_slowmo("...<<distant radio static>>..", (15, 120), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"Team Alpha! Hold, I hear something..\" ", (15, 150), fill = False)
    text_slowmo("....... ", (15, 180), fill = False)
    text_slowmo("... <<static>> ... ", (15, 210), fill = False)    
    text_slowmo("(???):  ... \"hel-\" ... ", (15, 240), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"Its coming from the elevator shaft...\" ", (15, 270), fill = False, speed=.07)

    escaping_sanctum2 = ask("\nWhat will you do next?\n\
    [Select 1, 2, 3, or 4 then press <enter> ]\n\n\
    1) Use the main stairs and search the basement?\n\
    2) Head towards the emergency exit through the lab?\n\
    3) Climb the stairs to the roof access point?\n\
    4) Rappel down the elevator shaft? \n\n>>> ", (5, 330), fill = False)
    if escaping_sanctum2 == "1":
        time.sleep(quick)
        basement(ETS_user)
    elif escaping_sanctum2 == "2":
        time.sleep(quick)
        lab(ETS_user)
    elif escaping_sanctum2 == "3":
        time.sleep(quick)
        roof(ETS_user)
    elif escaping_sanctum2 == "4":
        text_slowmo(f"{ETS_user.user_name} leads the Team towards the center elevator and peers into the darkness below ", (5, 10))
        text_slowmo(f"({ETS_user.user_name}): \"Thats a long way down...hook me up to that safety latch. I'm going down. Cover me\" ", (15, 50), fill = False)
        text_slowmo(f"After securing the tactical rope, {ETS_user.user_name} slowly makes their decent..\
Once inside the poorly lit elevator shaft, a small sign comes into view.....", (5, 120), fill = False, sleep = slow)
        pause()
        text_slowmo(f"WARNING: MAXIMUM WEIGHT FOR LATCH {(int(ETS_user.user_weight)-20)} LBS... ", (5, 200), box = True, speed = .1)
        text_slowmo("       SNAP!\n", (5, 250), fill = False)
        header()
        retry = ask("Game over. Try again? (Y/N):\n>>> ")
        if retry == "n" or retry == "N":
            sys.exit()
        else:
            escaping_sanctum(ETS_user)
    else:
        write("Invalid response", sleep = step)
        main_lobby(ETS_user)




############## Basement choice ###############################################
##############################################################################
##############################################################################

def basement(ETS_user):
    text_wrap("  Basement  ",(215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Alpha Team heads toward the frosted glass doors that lead to the stairs, the basement many flights down. \
With a slight push of the doors, radio static can be fainlty heard emanating from below. {ETS_user.user_color.title()} lights illuminate ascending \
and decending steps, but the team heads towards the noise.. ", (5, 10), sleep = slow*2)
    text_slowmo(f"({ETS_user.user_name}): \"We need to rendezvous with Bravo and figure out what happened here. Maybe the storm is interf- ", (15, 100), fill = False)
    flash_text("!!!!fffffffffffffffffffffffff \
ffffffssssssssssssssssssssssssss \
sssssshhhhhhhhhhhhhh!!!!!!! ",)
    text_slowmo("Every piece of radio equipment on Team Alpha bursts into noise, echoing throughout the landings above. ", (5, 10))
    text_slowmo(f"({ETS_user.user_name}): \"What the-- Comms off, turn comms off! ..We're going deaf and blind at this point\" ", (15, 60), fill = False)
    text_slowmo((f"There are no sounds but footsteps. Team Alpha reaches the basement level where {ETS_user.user_name} \
finds a radio on the ground. The lost radio is badly damaged, deep grooves are scratched into the surface. \
But the battery pack is missing.... There is a directory on the wall "), (5, 120), fill = False, sleep = slow)

    ##### Both choices 1&2 fork off in basement #########################################
    #################################################################################

    basement_fork_one = ask("What direction will you take Team Alpha? \n\
[Select 1 or 2, then press <enter> ]\n\n\
1) Right: \'Boiler Room\'\n\
2) Left: \'Electrical Power System\'\n\n>>> ", (5, 220), fill = False)

    if basement_fork_one == "1":
        time.sleep(step)
        boiler_room(ETS_user)
    elif basement_fork_one == "2":
        time.sleep(slow)
        electrical_room(ETS_user)
    else:
        write("invalid response", sleep = slow).upper()
        time.sleep(step)
        basement(ETS_user)

def boiler_room(ETS_user):
    boiler_keys = []
    temperature = 65
    text_wrap(" Boiler Room  ",(215, 40), font_size = 30, sleep = slow)
    text_slowmo("As Alpha Team enters the boiler room...\
There is a loud hissing noise coming from the pipes. ", (5, 10), sleep = slow)
    zombie_battle(ETS_user)
    text_slowmo(f"({ETS_user.user_name}): \"The zombies must have caused damage to the pipes\
we need to head to the boiler room in order to figure out what is going on...\" ", (15,10))
    text_slowmo("There is a bloated body in the corner of the room in a pool of blood. A ring of keys lays on his chest.\
Strange symbols are on the keys.... ", (5, 80), fill = False, sleep = slow)
    text_slowmo(f"({ETS_user.user_name}): \"These aren\'t normal keys...\" ", (15, 180), fill = False, sleep = slow)
    boiler_keys.extend(boiler_keys_full)
    while temperature < 125:
        text_slowmo(f"The current room temperature is {temperature} degrees ", (5, 10))
        z = 0
        for key in boiler_keys:
            z += 30
            text_wrap(key, (5, 50+z), fill = False, sleep = step)
        user_key = ask("What key do you want try?:  \n>>> ".lower(), (5, 220), fill = False)
        if user_key in boiler_keys:
            pass
        else:
            write("you entered the wrong key! please enter the correct key! ".upper(), sleep = step)
            continue
        if user_key == "blood":
            text_slowmo("Alpha Team chose the correct key after examining the boiler room. \
After inspecting the entire room, there is no sign of any damage to the pipes. ", (5,10))
            text_slowmo(f"({ETS_user.user_name}): \"I really thought we would find something in the boiler room. ", (5, 80), fill = False)
            text_slowmo("Alpha team growns impatient as communication issues persist and while trying to locate with \
bravo team before it's too late. The Team continues onward deeper to explore the basement. \
They find a door that leads to the ELECTRICAL ROOM ", (5, 200), fill = False, sleep = slow)
            electrical_room(ETS_user)
            break
        else:
            temperature += 20
            boiler_keys.remove(user_key)
            text_slowmo(f"{ETS_user.user_name}\'s notices there is a WARNING ALARM for increasing temperature. ", (5, 350), fill = False)
            text_wrap("\"The Door is Still Locked\" ", (5, 390), fill = False, sleep = slow)
    if temperature == 125:
        text_slowmo(f"The current room temperature is {temperature} degrees ".upper(), (5, 10))
        text_slowmo("The Room is engulfed in flames!!!!", (5, 50), fill = False, sleep = slow)
        text_slowmo("You have burned Alpha Team!!! Game Over ", (5, 100), fill = False)
        retry = ask("Try again? (Y/N) \n>>> ".lower(), (5, 220), fill = False)
        if retry == "n" or retry == "N":
            sys.exit()
        elif retry == "y" or retry == "Y":
            escaping_sanctum(ETS_user)
        else:
            time.sleep(step)
            write("Invalid response", sleep = slow)
            boiler_room(ETS_user)

def door_damage():
    damaging = ask("  press <enter> to break the door!!! ", (5, 100), allow_empty=True)
    text_wrap("  press <enter> to break the door!!! ", (5, 100), color = "black", fill = False)

def hit_door_hp(door_hp = 25): 
    while door_hp > 0:          
        door_damage()
        door_hp = door_hp - 5
        if door_hp != 0:
            text_slowmo(f"You have weakened the door down to {door_hp}% of its strength ", (5, 200))
        else:
            text_slowmo(f"\"WARNING!!! Failure!!! WARNING!! Door is it at {door_hp}%.\" You have broken through the door!!! ", (5, 240), fill = False)
    return door_hp

def electrical_room(ETS_user):
    random_lever_choice = random.choice(lever_direct)
    text_wrap(" Electrical Room", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"As the Alpha team enters the Electrical Room, they realize that the zombies have been \
jamming the communications all along. In the control room is an emgercy communication circuit breaker. \
{ETS_user.user_name} notices a lever that control the circuit. ", (5, 10))

    pause()
    attempts = 0
    while attempts < 3:
        lever_input = ask("\nWhich direction do you want to pull the lever?\n\
            [\"left\",\"right\", \"up\", \"down\"]\n\n>>> ", (5, 100), fill = False).lower()
        if lever_input in lever_direct:
            pass
        else:
            text_slowmo("You entered a wrong direction! Please try again ", (5, 300))
            continue
        if random_lever_choice == lever_input: 
            text_slowmo(f"You chose '{lever_input}''.The correct choice was '{random_lever_choice}'. \
The power hums as the generator is being restored ", (5,10), sleep = slow)
            break
        else:
            attempts += 1
            write("Nothing Happened", sleep = step)
            write("Nothing Happened", color = "black")
    if attempts == 3:
            text_slowmo("The lever cracks, trapping team Alpha in the room. ", (5, 300), sleep = slow)
            header()
            retry = ask("\nGame Over. Try again? (Y/N)\n>>> ", (5, 350), fill = False)
            if retry == "n" or retry == "N":
                sys.exit()
            elif retry == "y" or retry == "Y":
                escaping_sanctum(ETS_user)
            else:
                time.sleep(step)
                write("Invalid response").upper()
                electrical_room(ETS_user)
   
    text_slowmo("As the power restores, the door leading to the next corridor locks ", (5, 50), fill = False, sleep = slow)
    hit_door_hp()
    
    text_slowmo("Team Alpha breaks through and enters the corridor ", (5, 10))
    basement_fork_two = ask(f"{ETS_user.user_name}, what direction will you take Team Alpha? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Right: \'Freezer Section: Unit B\'\n\
    2) Straight: \'Dry Storage: Unit A\'\n\n>>> ", (5, 40), fill = False)
    if basement_fork_two == "1":
        time.sleep(step)
        basement_unitB(ETS_user)
    elif basement_fork_two == "2":
        time.sleep(step)
        basement_unitA(ETS_user)
    else:
        write("invalid response", sleep = slow)
        electrical_room(ETS_user)    


### Basement - choice 2 (Storage A) #########################################################
#############################################################################################


def basement_unitA(ETS_user):
    text_wrap("Basement: Unit A  ",(215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Team Alpha continues slowly down the corridor towards the storage bay. The staircase lights become less and less \
useful with each step as they head further into darkness. The only thing visible in the distance is a small window hovering on the door of \
Storage Unit A. The dim {ETS_user.user_color} light creeping through is barely visible, but the shadow of a figure flashes past... ", (5, 10))
    pause()
    text_slowmo(f"{ETS_user.user_name} quickens their step and readies Alpha Team to breach the door. ", (5, 100), fill = False, sleep = slow)
    text_slowmo(f"({ETS_user.user_name}): \"On my mark\". .(motions).. .3.. ........ ..2... ............ 1.. ", (5, 160), fill = False)
    text_wrap("            BANG! ", (200, 200), sleep = slow)
    pause()
    text_slowmo("Behind the Storage A doors lies Bravo Team. Some are injuried but all are accounted for. ", (5, 10))
    text_slowmo(f"({ETS_user.bravo_leader}): \"You look spooked, but aren\'t we glad to see you, {ETS_user.user_name}\" ", (5, 80), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"You don\'t look so hot either. Come on, let\'s get out of this place\" ", (5, 110), fill = False)
    pause()
    text_slowmo("Both teams return to the surface using a freight elevator. The shore where they left their boats is \
a ruin of vegetation and sand. The hum of engines roar over the sound of waves crashing against the vehicles. An \
injured Bravo squad member peers into the greycast sky, their hand covering a curious wound on their arm...... \
a deep bite wound. The outline of Toro Sanctum is reflected off their gaze as they look back at the shrinking island. ", (5, 10))
    text_slowmo("To be continued??? ", (250, 300), sleep = slow*2, fill = False)

### Basement - Choice 1 (Storage B) ###########################################################
###############################################################################################

def basement_unitB(ETS_user):
    text_wrap("Basement: Unit B", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Team Alpha makes a right and heads towards the frozen storage. The flickering {ETS_user.user_color} lights overhead \
crack and blink as they approach the freezer door. Through the icy window, there is a blinking LED light glowing on the ground in \
the darkness. The LED light is the same as on everyone\'s radio. ", (5, 10), sleep = slow)
    pause()
    text_slowmo(f"{ETS_user.user_name} grasps the frozen handle and pulls the door open slowly...taking a small step inside. Just as \
{ETS_user.user_name} grabs the lost radio, a hand lunges out of the darkness, grabbing their wrist ", (5, 120), fill = False)
    text_slowmo(f"({ETS_user.user_name}): ...\"What th------!\" ", (15, 180), fill = False, speed = .2)
    pause()
    text_slowmo(f"The freezer door slams shut, several locks forced in place. \
The slow flashing LED light tints the faces of zombies engulfing {ETS_user.user_name}... ", (5, 300), sleep = slow)
    Dead_team_member_battle(ETS_user)
    header()
    text_slowmo(" Game Over ", (5, 300), speed = .75)
    retry = ask("Try again? (Y/N)\n>>> ", (5, 325), fill = False)
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        write("Invalid response".upper())
        basement_unitB(ETS_user)



############## Lab Choice ##########################################
####################################################################
####################################################################

def lab(ETS_user):
    correct_wire = random.choice(wires_full)
    text_wrap(" Laboratory ", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Alpha Team begins to make their way towards the sealed {correct_wire} glass doors of the laboratory wing. \
The powerless automatic doors are pushed open with ease as Team Alpha enters the decontamination area. There is a sudden rumble felt... \
From many levels below comes the sound of heavy machinery and gears slowly grinding to a halt. ", (5, 10), sleep = slow)
    text_slowmo(f"({ETS_user.user_name}): \"What is going on here? It sounds like someone..\" ", (15, 140), fill = False)
    text_slowmo(f"{ETS_user.user_name} peers back towards the lobby as the decontamination doors lock into place. Alpha Team can see flashing \
{ETS_user.user_color.title()} lights overhead as the air is slowly pulled out of the room. ", (5, 200), fill = False)
    pause()
    text_slowmo(f"Near the wall is an emergency shut off switch, with wires exposed. {ETS_user.user_name} rushes over to examine the switch ", (5, 280), fill = False)
    cuts = 0
    wires = []
    wires.extend(wires_full)
    while cuts < 3:
        text_slowmo(f"({ETS_user.user_name}): \"We have to shut this damn thing down!\" ", (5, 10), sleep = step)
        z = 0
        for wire in wires:
            text_wrap(wire, (5, 50+z), color = wire, fill = False, sleep = step)
            z += 25
        user_wire = ask("What color wire will you cut:  \n>>> ".lower(), (5, 240), fill = False)
        if user_wire in wires:
            pass
        else:
            write(f"{ETS_user.user_name} rubs their eyes, they didn't select the right wire! ", (5, 300), sleep = slow)
            continue
        if user_wire == correct_wire:
            text_slowmo("The decontamination chamber doors open and oxygen is pumped back into the room. ", (5, 50), sleep = slow, speed = .07)
            break
        else:
            cuts += 1
            wires.remove(user_wire)
            text_slowmo("Beep ...... beep ..... beep.... ", (5, 280), speed = .07)
            text_slowmo("\"nothing happened\" ", (5, 310), sleep = slow, fill = False)
    if cuts == 3:
        text_slowmo(f"{ETS_user.user_name}\'s vision becomes blurry as the room reaches 0% oxygen level, coughing, Team Alpha falls to the ground ", (5, 280), sleep = slow)
        text_slowmo("Game Over ", (5, 320), fill = False, sleep = step)
        retry = ask("Try again? (Y/N)\n>>> ".lower(), (5, 360), fill = False)
        if retry == "n" or retry == "N":
            sys.exit()
        elif retry == "y" or retry == "Y":
            time.sleep(step)
            escaping_sanctum(ETS_user)
        else:
            time.sleep(step)
            write("Invalid response ".upper())
            lab(ETS_user)
    text_slowmo(f"Team Alpha stumbles on while catching their breath. The cooridor to the Lab is empty and appears untouched. The laboratory doors \
slide against a gritty floor. The lab is field of broken glass and debris. {ETS_user.user_color.title()} light is scattered in every direction as the team \
moves toward the emergency exit. The emergency exit doors are blocked by a mountain of large boxes, lab equipment, and garbage ", (5, 50))
    pause()
    if ETS_user.user_item == "A lucky coin" or ETS_user.user_item == "A golden locket" or ETS_user.user_item == "A bronze compass":
        text_slowmo(f"{ETS_user.user_item} falls out of {ETS_user.user_name}\'s pocket and rolls out of the lab entrance, making it to the corridor ", (5, 150), fill = False, sleep = step)
        text_slowmo(f"({ETS_user.user_name}): \"...strange..\" ", (5, 200), fill = False, sleep = step)
    else:
        pass

    lab_fork = ask(f"{ETS_user.user_name}, what will you do next? \n\
    [Select 1 or 2, then press <enter> ]\n\n\
    1) Onward: \'Dig out emergency exit\'\n\
    2) Go back: \'Return to lobby and take stairs to basement\'\n\n>>> ", (5, 240), fill = False)
    if lab_fork == "1":
        time.sleep(step)
        lab_onward(ETS_user)
    elif lab_fork == "2":
        time.sleep(slow)
        lab_flee(ETS_user)
    else:
        write("invalid response".upper(), sleep = slow)
        lab(ETS_user)

#### Lab option A - Game over          ##############################
#####################################################################

def lab_onward(ETS_user):
    text_wrap(" Laboratory: Emergency Exit ", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"The Team begins unblocking the emergency exit doors. The massive equipment pieces take the \
entire team to move aside. Shards of glass fall off of repositioned boxes. Something catches {ETS_user.user_name}\'s eye. ", (5, 10))
    pause()
    text_slowmo("Among the glass are pieces of shredded flesh and clumps of hair ", (5, 60), fill = False, speed = .07)
    text_slowmo(".. ........ .... ............. .. ", (5, 100), fill = False, sleep = step)
    text_slowmo(f"({ETS_user.user_name}): \"...... WAIT .... ALPHA TEAM FALL BAC------ ", (15, 130), speed = .07)
    zombie_battle(ETS_user)
    text_slowmo("The exit doors plunge open. Alpha team is bombarded, surrounded in seconds by dozens of screaming zombies ", (5, 150))
    header()
    retry = ask("Game Over. Try again? (Y/N)\n>>> ", (5, 280), fill = False)
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        write("Invalid response".upper())
        lab_onward(ETS_user)


### Lab option B - Chance to return to lobby ###############################################
############################################################################################

def lab_flee(ETS_user):
    text_slowmo(f"{ETS_user.user_name} guides Alpha Team back to the lobby and to the entrance of the main stairway ", (5, 20), sleep = slow)
    basement(ETS_user)


### Roof Choice ##########################################################
##########################################################################

def roof(ETS_user):
    roof_access = format(random.randint(0000,9999), '04d')
    text_wrap(" Rooftop ", (215, 40), font_size = 30, sleep = slow)
    text_slowmo(f"Team Alpha led by {ETS_user.user_name} heads towards the staircase and starts the long climb to the roof \
access door. The light becomes dimmer and dimmer as they ascend, the faint outline of a large metal door seems further away with each step. \
The sound of rain and distant thunder can be felt humming behind the steel door. The door is being held open by something...  \
{ETS_user.user_name} reaches down and pushes the door slightly to grab the small object ", (5, 10), sleep = step)
    text_slowmo(f"({ETS_user.user_name}): \"What is this? It looks like a small bone... ", (15, 140), fill = False, sleep = step, speed = .07)
    text_slowmo(f"The Team kicks open the door and rushes the rooftop. In every direction are bullet casings and empty ammunition \
crates. The helicopter on the helipad is destroyed; a twisted metal skeleton with it\'s propellers folded. The AH-{(str(roof_access)[:2])} \
Apache helicopter is military grade...The team moves further onto the roof when the metal door behind them slams shut ", (5, 10), sleep = step)
    pause()
    text_slowmo("The door is reinforced steel with a blinking keypad above the door handle. ", (5, 140), fill = False, sleep = step)
    text_slowmo("[ _ _ _ _ ] ", (5, 180), fill = False, speed = .07, sleep = step)
    text_slowmo(f"({ETS_user.user_name}): \"Dammit! The keypad barely has power supply!\" ", (15, 210), fill = False, sleep = slow)
    attempt_count = 0
    while attempt_count < 3:
        text_slowmo(f"Still gripping the small bone, {ETS_user.user_name} feels something carved into it. There are a series of numbers but some are \
too difficult to make out. All that is legible is \"_ _ {(str(roof_access)[2:])}\" ", (5, 10))
        roof_attempt = ask("Enter the correct access number:\n>>> ", (5, 80), fill = False)
        if roof_attempt == roof_access:
            text_slowmo("<<<Access granted>>> ", (5, 100))
            pause()
            text_slowmo(f"The team rushes through the door and races down the steps in growing darkness. {ETS_user.user_name} shuts the heavy \
door just as decayed arms and hands are within reach. The team heads straight to the basement just as a figure comes into view on the next landing. ", (5, 130), fill = False, sleep = step)
            zombie_battle(ETS_user)
            basement(ETS_user)
            break
        else:
            attempt_count += 1   
            write(" <<<Access Denied>>> ", (5, 100), sleep = 1)
            text_slowmo(f"Sparks shoot from the AH-{(str(roof_access)[:2])} Apache helicopter ", (5, 10), sleep = slow)
    if attempt_count == 3:
        text_slowmo(f"An alarm blares from the rooftop and echoes throughout the island. The access door keypad flashes {ETS_user.user_color} \
as smoke rises from the power circuit. The alarm continues on as flocks of birds scatter off of distant tree tops. As the sirens screech...a closer \
sound becomes audible...", (5, 10), sleep = step)
        pause()
        text_slowmo("..........Hrrrrrnnnnggggg.... ", (5, 100), fill = False, sleep = step, speed = .07)
        text_slowmo(f"({ETS_user.user_name}): \"What the ----- ", (5, 130), fill = False, sleep = slow)
        text_slowmo(f"All at once, dozens of zombies rise up and slowly head towards team Alpha. {ETS_user.user_name} punches \
the access panel and shuts off the alarm system. The zombies move closer and closer to the team ", (5, 10), sleep = step)
        text_slowmo(f"The team heads to the rooftop ledge and stares down at the concrete below. With no choice left, {ETS_user.user_name} \
orders the team to rappel down to the nearest window ", (5, 100), fill = False, sleep = slow)
        roof_escape(ETS_user)
        

def roof_escape(ETS_user):
    text_wrap(" Rooftop Escape ", (200, 40), font_size = 30, sleep = slow)
    text_slowmo(f"The sound of harnesses zipping down the rappel lines buzz like a thousand angry wasps. The team soars down and lunges inside \
the nearest row of windows several landings below. Crashing through glass, {ETS_user.user_name} disconnects the rappel line and lands on a \
concrete surface. The room is dark and humid, the air acrid. ", (5, 10), sleep = step)
    pause()
    text_slowmo(".................... ", (15, 120), fill = False)
    text_slowmo("....................", (15, 150), fill = False, sleep = step)
    text_slowmo(f"({ETS_user.user_name}): Something's not right in here...\" ", (15, 180), fill = False, sleep = slow)
    text_slowmo("(???): ........... hhhHHHHRNNNGAAA!!! ", (15, 210), fill = False, sleep = step, speed = .07)
    pause()
    text_slowmo(f"{ETS_user.user_name} raises a flashlight and illuminates the faces of a zombie hoard rushing toward Team Alpha.. ", (5, 10), sleep = slow)
    header()
    retry = ask("Game Over. Try again? (Y/N)\n>>> ", (5, 280), fill = False)
    if retry == "n" or retry == "N":
        sys.exit()
    elif retry == "y" or retry == "Y":
        time.sleep(step)
        escaping_sanctum(ETS_user)
    else:
        time.sleep(step)
        write("Invalid response".upper())
        roof_escape(ETS_user)

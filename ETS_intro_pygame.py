from pygame_utilities import *
from ETS_battles_pygame import *
from ETS_functions_pygame import *
import time
import pygame


def introduction(ETS_user):
    pause()
    text_slowmo("A single flash of lightning casts dozens of long shadows across the skybridge. The subsequent \
thunder crashes, deafening the small group. The rain is relentless, making the view in every direction a grey abyss. \
The only feature made out in the distance, as another flash of lightening blazes across the sky, is the outline \
of a gigantic building. An entire team has been missing from the rendezvous for the better part of an hour. \
Someone is shouting over the rain, gripping a radio... ", (5, 10), sleep = slow)

    text_slowmo(f"({ETS_user.user_name}): \"....-repeat, Systems check! Over!\" ", (15, 220), fill = False)
    text_slowmo(" ...... ", (15, 250), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"...Systems check, come in Team Bravo!\" ", (15, 290), fill = False)
    text_slowmo("... (radio silence) ... ", (15, 320), fill = False)
    text_slowmo(".... <<<static>>> ", (15, 350), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"BRAVO, DO YOU READ???!!!\" ", (15, 380), fill = False)
    text_slowmo("... (radio silence) ... ", (15, 410), fill = False)
    text_slowmo(f"({ETS_user.user_name}): \"Damn!! Alpha, move out!\" ", (15, 440), fill = False)

    pause()
    
    text_slowmo(f"Rain continues to pour in sheets as Alpha team scans the lobby of Toro Sanctum, a newly constructed \
bioengineering facility on {ETS_user.user_city.title()} Island. After the \"Incindent\", the paramilitary contractors of PiThon were \
flown in from {ETS_user.user_country} to inspect Toro Sanctum and the surrounding coast. Team Bravo led the expedition \
into the facility while Team Alpha scanned the ports of entry and docks. There was nothing. No signs of anyone \
having visited or worked in the high tech research facility which celebrated its launch two weeks ago. No ships. \
No vehicles on the newly paved parking lots. Nothing. Team Alpha lost communication with Bravo squad just as the \
storm starting picking up. With limited visibility, Team Alpha rushes past the deserted security gates and double \
pane glass doors of Toro Sanctum. The lobby is a massive cavern of steel and glass, abandoned and dimly lit. The rain \
drums on the glass overhead as Team Alpha steps further into the facility... ", (5, 10), sleep = slow)
    
    pause()
    

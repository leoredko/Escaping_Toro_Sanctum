# Escaping Toro Sanctum
Our game is Escaping Toro Sanctum(ETS). It was worked on by Tyler Toro, Lavonte Carter, and Leo Redko.
It is a text-based adventure game that lets the user choose their own path with varying outcomes. The story takes place on an island in which the player searches for a missing team. 

One major challenge we overcame was simplifying the code, variable scoping across multiple files, and calling functions. We were able to use Python class mechanisms to initialize a user class, called Player(), which allowed us to easily take in user input and later calling these into functions across all game files. 

Our group name is LaborisGloriaLudi, which means "Games are the Glory of Work"


## How to run and install Escaping Toro Sanctum

For the purposes of running the game successfully, makes sure to clone this repository into a clean directory. All files should be saved into this folder to function properly. All the code is written in Python version 3.9.4 and can be ran through a local terminal; all python libraries/modules listed below must be installed for Escaping Toro Sanctum to be ran *(except pytest)*. 

## Main Branch Files 

### Escaping_Toro_Sanctum.py 
This is the main game file. ***Please run this file to start the game.***

### ETS_intro.py
This is the backstory and introduction to the game

### ETS_functions.py
This file holds the functions that let the game run properly

### ETS_rooms.py
This large file is comprised of game locations and puzzles

### functions_test.py
This file is soley for unit testing purposes and is not utilized to run ETS

### ETS_battles.py
This file is comprised of game enemy classes and battle functions


## Python Libraries/Modules used

We used the following **libraries** in our project: 
- Numpy
    Used to randomize puzzle output to ensure each game experience is unique
- Sys
    Used to manipulate the python environment
- Time
    Used to manipulate speed of text output and delays to the terminal
- Colorama
    Used to change character color via the terminal
    - Fore  *changes character foreground text color*
    - Init  *initializes colorama*
- OS
    Used to create paths and use functions with the current operating system

- Pytest *unit testing code/functions*
    - Builtins
        To gain access to built-in modules or when working with similiarly named functions
    - Mock
        Used to simulate user input in a test environment





### File Architecture: Below is a diagram of our game files and how the User Class is utilized throughout the other files. In addition, the diagram shows the relationship between the Functions file. 

![ETS - Game Architecture](https://user-images.githubusercontent.com/78003415/115936886-744fbe00-a464-11eb-9387-94eed2140ec6.png)


### Below is a flow chart of the game storyline.
![ETS - Storyline flow chart](https://user-images.githubusercontent.com/78003415/116010009-80fe1e80-a5ea-11eb-9c7c-1b21f5e5f091.png)

# imports all necesary modules
import pygame
import sys
from pygame.locals import *
import math

# initializes pygame
pygame.init()

# initializes the screen
screen = pygame.display.set_mode((750, 480), pygame.NOFRAME)

# creates background color
screen.fill((255, 245, 204))

# imports all textures
dot = pygame.image.load(r'dot.png')
dash = pygame.image.load(r'dash.png')
dashup = pygame.image.load(r'dashup.png')
lineup = pygame.image.load(r'lineup.png')
line = pygame.image.load(r'line.png')
red = pygame.image.load(r'red.png')
blue = pygame.image.load(r'blue.png')

# creates done, turn, and x y variables
done = False
x = 0
y = 0
turn = 0

# creates score counting variables
rscore = 0
bscore = 0

# creates horizontal lines for the grid
while x < 8:
    while y < 6:
        screen.blit(dash,(-10 + x*90,-10 + y *90))
        y = y + 1
    x = x + 1
    y = 0
x = 0

# creates vertical lines for the grid
while y < 5:
    while x < 9:
        screen.blit(dashup,(-10 + x * 90,-10 + y *90))
        x = x + 1
    y = y + 1
    x = 0
y = 0

# creates dots for the grids
while x < 9:
    while y < 6:
        screen.blit(dot,(x*90,y*90))
        y = y + 1
    x = x + 1
    y = 0
x = 0

# prints out initial turn statement
print("Red's turn")

# Creates the gameplay loop
while done == False:
    for event in pygame.event.get():
        
        # create mx and my variables
        mx, my = pygame.mouse.get_pos()
        a = mx // 90
        b = my // 90

        # detects mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            """Checks if the left mouse button has been pushed"""
            if event.button == 1:
                """Checks if the player wants to take a vertical line"""
                if math.isclose(mx, a * 90, abs_tol = 50) == True:
                    """Checks if mouse is close enough to a line to be a valid input"""
                    if math.isclose(mx, a * 90, abs_tol = 40) == True:
                        """Displays the line in the game"""
                        screen.blit(lineup,(-10 + a * 90, b * 90))
                        """Adds to the turn counter to change turns to the other player"""
                        turn = turn + 1
                    """Detects and prints out a statement if move is not valid"""
                    if math.isclose(mx, a * 90, abs_tol = 35) == False:
                        print("Please make a valid move")
                """Checks if the player wants to take a horizontal line"""
                if math.isclose(mx, a * 90, abs_tol = 50) == False:
                    """Checks if mouse is close enough to a line to be a valid input"""
                    if math.isclose(my, b * 90, abs_tol = 40) == True:
                        """Displays the line in the game"""
                        screen.blit(line,(+ a * 90, b * 90 - 10))
                        """Adds to the turn counter to change turns to the other player"""
                        turn = turn + 1
                    """Detects and prints out a statement if move is not valid"""
                    if math.isclose(my, b * 90, abs_tol = 40) == False:
                        print("Please make a valid move")
            """Prints out who's turn it is"""
            if turn % 2 == 0:
                print("Red's turn")
            if turn % 2 == 1:
                print("Blue's turn")
            """Detects if the right mouse button has been pushed"""
            if event.button == 3:
                """Checks if it's player ones turn"""
                if turn % 2 == 0:
                    """Claims box"""
                    screen.blit(red,(12 + a * 90 ,12 + b * 90))
                    """Adds to red score counter"""
                    rscore = rscore + 1
                """Checls if it's player twos turn"""
                if turn % 2 == 1:
                    """Claims box"""
                    screen.blit(blue,(12 + a *90,12 + b *90))
                    """Adds to blue score counter"""
                    bscore = bscore + 1
        """Creates a function that ends the game"""
        while rscore + bscore == 40:
            """Checks and prints if red wins"""
            if rscore > bscore:
                print("RED WON")
                done = True
                quit()
            """Checks and prints if blue wins"""
            if bscore > rscore:
                print("BLUE WON")
                done = True
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_q:
                quit()
    
    """Refreshes the screen"""
    pygame.display.flip()
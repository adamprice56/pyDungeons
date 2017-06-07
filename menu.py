import sys

import random as rnd
import time
import fates


pathOptions=["Water", "Air", "Fire", "Earth"]
pathAttributes=["Cold", "Windy", "Hot", "Solid"]

# Set up variables
 
isPlaying = ""
playing = False

global health
moveshown = bool()

def menu():
    print("Welcome")
    print("##################################")
    print("# Welcome to a not very dungeony #")
    print("# and dragonny game!             #")
    print("##################################")
    print()
    print()
    setupgame()
    nextmove("N")

def showStats():
    global health
    print(" - " + "Health: " + str(health) + " - ")

def choice():
    validChoice = False
    while validChoice == False:
        choice = input("Enter your choice: ").upper()
        if choice == "A":
            validChoice = True
        elif choice == "B":
            validChoice = True
        else:
            print("Please choose A or B")
            
    return choice

def crossroad(road1, road2, selection):
    print("You come to a crossroad, You can go: " + road1 + " or " + road2)
    print("Choose an option below: ")
    #selection = choice()
    if selection != "N":
        determineSelection(selection)
    

def door(door1, door2, selection):
    print("You've reached 2 doors, " + door1 + " and " + door2 + ".")
    print("Choose an option below: ")
    #selection = choice()
    if selection != "N":
        determineSelection(selection)


def determineSelection(selection):
    global health
    print("You chose: " + selection)
    print("Determining your fate...")
    seed = rnd.randint(0,5)
    seed2 = rnd.randint(0,1)
    time.sleep(1)
    health = fates.choiceVariety[seed](seed, seed2, health)


def doorOrRoad(seed, selection):
    
    if seed is 0:
        door("Door A", "Door B", selection),
    else:
        crossroad("Road A", "Road B", selection)

def checkHealth():
    global health
    if health < 25 and health > 0:
        print("Your health is low!")
    elif health is 0:
        print("You are dead!")
        input("Press any key to exit...")
        exit()
    else:
        pass

def setupgame():
    #global inventory = ["Sword", "Sheild"]
    global health
    health = 100

def checkstats():
    checkHealth()
    showStats()

def nextmove(selection):
    selectionSeed = rnd.randint(0,1)
    doorOrRoad(selectionSeed, selection)


def main(selection): 
 # Main loop
    global health

    try:
        health
    except NameError:
        print("ERROR: Health was not defined")
    else:

        if health > 0:
            checkHealth()
            showStats()
            nextmove(selection)
        else:
        #Player has 0 health - End game
            checkHealth()
    
        

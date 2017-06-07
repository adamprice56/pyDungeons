import random as rnd
import loot

def healthdrain(health):

    healthdrain = rnd.randint(0, health)
    newhealth = health - healthdrain
    
    print("You lost " + str(healthdrain) + " health!")

    return newhealth

def genbadinstance(seed, seed2, health):
    if seed2 is 0:
        print("A giaint Spider attacked you!")
        health = healthdrain(health)
    else:
        print("A skeleton stabbed you!")
        health = healthdrain(health)

    return health

def VeryBad(seed, seed2, health):
    print("That was a VERY bad choice.")
    health = genbadinstance(seed, seed2, health)
    return health

def Bad(seed, seed2, health):
    print("Bad stuff happened.")

def Neutral(seed, seed2, health):
    print("Meh, S'alright.")

def Good(seed, seed2, health): 
    print("That was a good choice.")

def VeryGood(seed, seed2, health):
    print("Very good choice!")

def Special(seed, seed2, health): 
    print("You found loot!")
    loot.genLoot()


choiceVariety = {
    0 : VeryBad,
    1 : Bad,
    2 : Neutral,
    3 : Good,
    4 : VeryGood,
    5 : Special,
}
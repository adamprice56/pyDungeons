import random as rnd

lootTypes = [
    "Weapon", 
    "Armour",
    "Money"
]

weapons = [
    "Sword",
    "Dagger",
    "Bow & Arrow"
]

weaponAttributes = [
    "Attack",
    "Defense",
    "Range",
    "Weight"
]

def genLoot():

    #Generate type e.g. Weapon, Armour, Money
    #Luck value determined by seed from the door/route just traversed
    typeID = rnd.randint(1,3)
    luck = rnd.randint(0,5)

    



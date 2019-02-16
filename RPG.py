import random
import os
import time


from src import rpgplayer
from src import fight
from src import items
clear = lambda: os.system('cls')



def start1():  # #Shows the player his stats
    clear()
    rpgplayer.player_health(PlayerIG)
    print(PlayerIG.name + ", the" + PlayerIG.race +'!\nStrength: ' + PlayerIG.stats['strength'] + "\nSpeed: " +
     PlayerIG.stats['speed'] + '\nFortitude: ' + PlayerIG.stats['fortitude'])
    option = input("1.) Fight\n2.) Shop\n3.) Inventory\n4.) Load\n5.)Exit\n")
    if option == "1":
        fight.Prefight(PlayerIG)
    elif option == "2":
        start1()
    elif option == "3":
        PlayerIG.playerinventory.view()
        start1()
    elif option == "4":
        pass
    elif option == "5":
        exit()
    else:
        start1()


def start():  # #asking player name and starting the code
    print("Hello what is your name?")
    option = str(input("-->"))
    prace = str(input('Please enter your race selection! details about each race are in the readme file: '))
    pjob = str(input('Please enter the class of your character! Details about each race are in the readme file: '))
    global PlayerIG
    PlayerIG = rpgplayer.Player(option,prace,pjob)
    sword = items.Weapon('Sword', 10, 1, 'Slash', 's')
    print(type(sword))
    PlayerIG.playerinventory.add(sword)
    start1()


def main():  # #Gives options to th1\e player. Still need a save feature
    print("Welcome to my game!\n")
    print("1.)Start\n2.)Load\n3.)Exit")
    option = str(input("-> "))
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        exit()
    else:
        main()


main()  # #Starts the game

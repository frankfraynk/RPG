import random


class Enemy:
    def __init__(self,lvl,dmg,strength,name,goldgain):
        self.lvl = lvl
        self.dmg = dmg
        self.strength = strength
        self.name = name
        self.goldgain= goldgain
        self.speed = random.randint(2,3)
        self.size = 2
        self.maxhealth = 20
        self.health = self.maxhealth


    def attackPlayer(self,player):
        print("Enemy is swinging!")
        hit_chance = random.randint(1,20) + (self.lvl/2)
        if hit_chance >= (10+player.armor):
            player.health = player.health - self.dmg
            print('The ' + self.name + ' hit you for ' + str(self.dmg) + ' using ' + self.dtype + '!')
        else:
            print("The " + self.name + ' missed!')
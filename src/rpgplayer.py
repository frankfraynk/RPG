from src.items import Inventory,Weapon,Armor

class Player: #Create a class for the player with different attributes
    def __init__(self, name,race,job):
      self.playerinventory = Inventory(self)
      self.strength = 10
      self.fortitude = 10
      self.speed = 10
      self.stats = {'strength':self.strength,'fortitude':self.fortitude,'speed':self.speed}
      stat_buy(self)
      if race == 'minotaur' or race == 'm':
        self.race = 'Minotaur'
        self.size = 2
        self.fortitude +=2
        self.strength +=1
      elif race == 'goblin' or race == 'g':
        self.race = "Goblin"
        self.size = 1
        self.stats['fortitude'] += 2
        self.stats['speed'] +=1
      elif race == 'wolfman' or race =='w':
        self.race = "Wolfman"
        self.size = 2
        self.stats['strength'] += 2
        self.stats['fortitude'] +=1
      elif race == 'darkelf' or race == 'd':
        self.race = "Dark Elf"
        self.size = 1
        self.stats['speed'] += 3
      elif race == 'ogre' or race == 'o':
        self.race = "Ogre"
        self.size = 2
        self.fortitude +=3
      if job == 'warrior' or job == 'w':
        self.job = 'Warrior'
        self.playerinventory.add(Weapon('Cutting Axe',10, self.size, 'Slash', 's'))
        self.playerinventory.add(Armor('Leather Tunic', 10, self.size,2))
        bab = 2


      self.name = name
      self.maxhealth = 1001
      self.health = self.maxhealth
      self.attack = self.strength
      self.attacks = []
      self.gold = 100
      self.pots = 0
      

health_dashes = 20
def player_health(player):
  dash_convert = int(player.maxhealth/health_dashes)
  current_dashes = int(player.health/dash_convert)
  remaining_health = health_dashes - current_dashes

  health_display = ''.join(['-' for i in range(current_dashes)])
  remaining_display = ''.join([' ' for i in range(remaining_health)])
  percent = str(int((player.health/player.maxhealth)*100)) + "%"

  print("|" + health_display + remaining_display + "|")
  print("         " + percent)


def stat_buy(self):
  

  print('Welcome to the stat buy! Each ability score starts at 10, and you get three modifiers to add to them, +2,+1,-1')
  p2mod = input('To which ability would you like to add the +2 modifier? (strength speed and fortitude)')
  if p2mod in self.stats.keys():
    self.stats[p2mod] += 2
    print(p2mod, "has been raised by two, totalling", self.stats[p2mod])
  else:
    prit('Invalid ability or value, try again')
    stat_buy()
  

  err = True
  while(err):
    err = False
    p1mod = input('To which ability would you like to add the +1 modifier?')

    if p1mod == p2mod or p1mod not in self.stats.keys():
      print('There has been an error in your selection, try again! (You can\'t apply more than one modifier to a particular ability)')
      err = True
      continue

    else:
      self.stats[p1mod] += 1
      print(p1mod, "has been raised by two, totalling", self.stats[p1mod])

  err = True
  while(err):
    err = False
    m1mod = input('To which ability would you like to add the -1 modifier?')

    if m1mod == p1mod or m1mod == p2mod or m1mod not in self.stats.keys():
      print('There has been an error in your selection, try again! (You can\'t apply more than one modifier to a particular ability)')
      err = True
      continue
    else:
      self.stats[m1mod] -= 1
    print(m1mod, "has been raised by two, totalling", self.stats[m1mod])





class Item:  # Constructor for items
    def __init__(self, name, cost, sizeclass):
        self.name = name
        self.cost = cost
        self.sizeclass = sizeclass
        self.equippable = False


class Weapon:
    def __init__(self, name, cost, sizeclass, attack, aType):
        self.name = name
        self.cost = cost
        self.sizeclass = sizeclass
        self.attack = attack
        self.aType = aType
        self.equippable = True


class Armor():
    def __init__(self, name, cost, sizeclass, defense,):
        self.name = name
        self.cost = cost
        self.sizeclass = sizeclass
        self.defense = defense
        self.equippable = True
class Inventory:
    def __init__(self, player):
            self.wslot = Weapon('Fists', 0, 0, 1, 'b')
            self.aslot = Armor('Loincloth', 0, 0, 1)
            self.storage = []
            self.player = player

    def view(self):  # function for viewing the player's inventory. currently includes the menu too
        print(type(self.wslot))
        print("Welcome to" + self.player.name + "'s' inventory, these are the items in their inventory: ")
        print("In storage: ")
        h = 1
        for vitem in self.storage:
            if isinstance(vitem, Weapon):
                print(str(h) + ': ' + vitem.name, vitem.cost, vitem.sizeclass, vitem.attack)
            else:
                print(str(h) + ': ' + vitem.name, vitem.cost, vitem.sizeclass)
            h += 1

        print("Equipped items: \nWeapon: " + self.wslot.name + "\nArmor: " + self.aslot.name)
        menu_input = input('would you like to (e)quip an item, (u)nequip an item, (v)iew an items details, or e(x)it: ')
        while menu_input != 'x':  # inventory menu, includes functionality for equipping, unequipping, and viewing an items details.


            if menu_input == 'e':  # menu item for equipping items

                e_i = int(input('input the index of the item you want to equip: ')) - 1
                if isinstance(self.storage[e_i], Weapon) or isinstance(self.storage[e_i], Armor):
                    self.equip(self.storage[e_i])

            elif menu_input == 'u':  # menu item for unequipping items
                u_input = input('Would you like to unequip your (w)eapon, or your a(r)mor: ')
                if u_input == 'w':
                    self.unequip(self.wslot)
                elif u_input == 'r':
                    self.unequip(self.aslot)

            elif menu_input == 'v':  # menu item for viewing the details of an item.
                pass
            menu_input = input('would you like to (e)quip an item, (u)nequip an item,'
                               ' (v)iew an items details, or e(x)it: ')



    def add(self, ita):
        self.storage.append(ita)


    def unequip(self, itu):
        if itu.name == self.wslot.name and itu.name != 'Fists':
            self.add(itu)
            self.wslot = Weapon('Fists', 0, 0, 1, 'b')
        elif itu.name == self.aslot.name and itu.name != 'Cloth':
            self.add(itu)
            self.aslot = Armor('Cloth', 0, 0, 1)

    def equip(self,ifs):
            if ifs in self.storage:
                print('item is in storage')
                if type(ifs) is Weapon:
                    if self.wslot.name != "Fists":
                        self.unequip(self.wslot)
                    self.wslot = ifs
                    print(ifs.name, "has been equipped!")
                    self.player.attacks.append(ifs.attack)
                    self.storage.pop(self.storage.index(ifs))
                elif type(ifs) is Armor:
                    if self.aslot.name != "Cloth":
                        self.unequip(self.aslot)
                    self.aslot = ifs
                    self.storage.pop(self.storage.index(ifs))
                else:
                    print('This item is not equippable or another error has occured in the type of item you\'re trying to e'
                     'quip. Item type is ' + str(type(ifs)))

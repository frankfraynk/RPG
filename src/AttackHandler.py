import random as ran
#a is attacker, r is recipient
def AHandler(a,r,attack):
    print(a.name, "is trying to attack",r.name,'with', attack.name + "!")
    attackroll = ran.randint(1,attack.roll) + a.strength
    AC = 10 + r.armor + r.speed
    if attackroll >= AC:
        damageroll = ran.randint(1,attack.dmg) + a.stength
        r.health = r.health - damageroll
        print(a.name + "\'s", attack.name, "hit! Dealing", damageroll,'damage!')


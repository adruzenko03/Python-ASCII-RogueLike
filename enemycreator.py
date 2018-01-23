from random import *

class Enemy (object):

    def __init__(self, name, maxhp, strength, rarity, moneydrop):
        self.name = name
        self.maxhp = maxhp
        self.strength = strength
        self.rarity = rarity
        self.moneydrop = moneydrop

    def __str__(self):
        return ("%s, %d, %d, %s" % (self.name, self.maxhp, self.strength, self.rarity))


def load_enemy_file(file):

    enemyfile = open(file, "r")
    enemylist = []
    linelist = []

    for line in enemyfile:
        linelist.append(line.strip())

    while linelist[0] != "STOP":
        moneydrop = linelist[4].split("-")
        for m in moneydrop:
            m = int(m)
        enemylist.append(Enemy(linelist[0], int(linelist[1]), int(linelist[2]), linelist[3], moneydrop))
        for x in range(0, 6):
            del(linelist[0])

    return enemylist

def get_random_enemy(enemylist):

    posslist = []

    for x in enemylist:

        if x.rarity == "verycommon":
            for y in range(1, 13):
                posslist.append(x)

        if x.rarity == "common":
            for y in range(1, 7):
                posslist.append(x)

        if x.rarity == "uncommon":
            for y in range(1, 5):
                posslist.append(x)

        if x.rarity == "rare":
            for y in range(1, 3):
                posslist.append(x)

        if x.rarity == "veryrare":
            posslist.append(x)

    return choice(posslist)
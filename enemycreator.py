from random import *
from itemcreator import *
from copy import *

class Enemy (object):

    def __init__(self, name, maxhp, strength, weaponchoices, rarity, moneydrop):
        self.name = name
        self.maxhp = maxhp
        self.strength = strength
        self.weaponchoices = weaponchoices
        self.rarity = rarity
        self.moneydrop = moneydrop
        self.weapon = None

    def get_random_weapon(self):
        try:
            self.weapon = deepcopy(Item("Unarmed Attack", "attack", "...", "weapon", [int(self.weaponchoices[1]), int(self.weaponchoices[2])]))
        except:
            w = choice(self.weaponchoices)
            itemfile = load_item_file("items.txt")
            for i in itemfile:
                if i.id == w:
                    self.weapon = deepcopy(i)


    def __str__(self):
        return ("%s, %d, %d, %s" % (self.name, self.maxhp, self.strength, self.rarity))


def load_enemy_file(file):

    enemyfile = open(file, "r")
    enemylist = []
    linelist = []

    for line in enemyfile:
        linelist.append(line.strip())

    while linelist[0] != "STOP":

        moneydrop = linelist[5].split("-")
        for m in moneydrop:
            m = int(m)

        weaponlist = []
        weapons = linelist[3].split(", ")
        for w in weapons:
            if w[0] == "A":
                w = w[7:]
                r = w.split("-")
                weaponlist = ["ATTACK", r[0], r[1]]
            else:
                weaponlist.append(w)

        enemylist.append(Enemy(linelist[0], int(linelist[1]), int(linelist[2]), weaponlist, linelist[4], moneydrop))
        for x in range(0, 7):
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
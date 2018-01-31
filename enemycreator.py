from random import *
from itemcreator import *
from copy import *

class Enemy (object):

    def __init__(self, name, maxhp, strength, weaponchoices, rarity, moneydrop, droplist):
        self.name = name
        self.maxhp = maxhp
        self.strength = strength
        self.weaponchoices = weaponchoices
        self.rarity = rarity
        self.moneydrop = moneydrop
        self.droplist = droplist
        self.weapon = None

    def get_random_weapon(self):
        try:
            self.weapon = deepcopy(Item("Unarmed Attack", "attack", "...", "weapon", 0, None, [int(self.weaponchoices[1]), int(self.weaponchoices[2])]))
        except:
            w = choice(self.weaponchoices)
            itemfile = load_item_file("items.txt")
            for i in itemfile:
                if i.id == w:
                    self.weapon = deepcopy(i)

    def get_random_drops(self, player):
        itemfile = load_item_file("items.txt")
        for a in self.droplist:
            chance = randint(1, 100)
            if chance >= 100-a[0]:
                del(a[0])
                item = choice(a)
                for i in itemfile:
                    if i.id == item:
                        player.inventory.append(deepcopy(i))

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

        itemdroplist = []
        items1 = linelist[6].split(" | ")
        for items2 in items1:
            items = items2.split(", ")
            itemdroplist.append([])
            for i in items:
                if i == items[0]:
                    itemdroplist[-1].append(int(i))
                else:
                    itemdroplist[-1].append(i)

        enemylist.append(Enemy(linelist[0], int(linelist[1]), int(linelist[2]), weaponlist, linelist[4], moneydrop, itemdroplist))
        for x in range(0, 8):
            del(linelist[0])

    return enemylist

def get_random_enemy(enemylist, level):

    posslist = []

    for x in enemylist:

        if x.rarity == "verycommon":
            if level <= 6:
                for y in range(1, 13-(level*2)):
                    posslist.append(x)

        if x.rarity == "common":
            if level <= 8:
                for y in range(1, 9-level):
                    posslist.append(x)

        if x.rarity == "uncommon":
            for y in range(1, 5):
                posslist.append(x)

        if x.rarity == "rare":
            for y in range(1, 3+level):
                posslist.append(x)

        if x.rarity == "veryrare":
            for y in range(1, 1+(level//2)):
                posslist.append(x)

    return choice(posslist)
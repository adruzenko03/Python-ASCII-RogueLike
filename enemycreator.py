class Enemy (object):

    def __init__(self, name, maxhp, strength, rarity):
        self.name = name
        self.maxhp = maxhp
        self.strength = strength
        self.rarity = rarity

    def __str__(self):
        return ("%s, %d, %d, %s" % (self.name, self.maxhp, self.strength, self.rarity))


def load_enemy_file(file):

    enemyfile = open(file, "r")
    enemylist = []
    linelist = []

    for line in enemyfile:
        linelist.append(line.strip())

    while linelist[0] != "STOP":
        enemylist.append(Enemy(linelist[0], int(linelist[1]), int(linelist[2]), linelist[3]))
        for x in range(0, 5):
            del(linelist[0])

    return enemylist
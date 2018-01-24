class Item (object):

    def __init__(self, name, id, desc, type, output):
        self.name = name
        self.id = id
        self.desc = desc
        self.type = type
        self.output = output

def load_item_file(file):

    itemfile = open(file, "r")
    itemlist = []
    linelist = []

    for line in itemfile:
        linelist.append(line.strip())

    while linelist[0] != "STOP":
        if linelist[3] == "weapon":
            l = linelist[4].split("-")
            for x in range(0, len(l)):
                l[x] = int(l[x])
            itemlist.append(Item(linelist[0], linelist[1], linelist[2], linelist[3], l))
        elif linelist[3] == "potion":
            itemlist.append(Item(linelist[0], linelist[1], linelist[2], linelist[3], int(linelist[4])))
        for x in range(0, 6):
            del(linelist[0])

    return itemlist
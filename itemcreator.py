class Item (object):

    def __init__(self, name, id, type, output):
        self.name = name
        self.id = id
        self.type = type
        self.output = output

def load_item_file(file):

    itemfile = open(file, "r")
    itemlist = []
    linelist = []

    for line in itemfile:
        linelist.append(line.strip())

    while linelist[0] != "STOP":
        if linelist[2] == "weapon":
            itemlist.append(Item(linelist[0], linelist[1], linelist[2], linelist[3].split("-")))
        elif linelist[2] == "potion":
            itemlist.append(Item(linelist[0], linelist[1], linelist[2], int(linelist[3])))
        for x in range(0, 5):
            del(linelist[0])

    return itemlist
class Room (object):

    def __init__(self, name, xl, yl, layout):
        self.name = str(name)
        self.xl = int(xl)
        self.yl = int(yl)
        self.layout = layout


def load_room_file(file):

    tr = open(file, "r")

    lay = []
    for line in tr:
        lay.append([])
        for tile in line:
            if tile != "\n":
                lay[-1].append(tile)

    return Room("Test Room", len(lay[0]), len(lay), lay)

def load_room_file_v2(file):

    roomfile = open(file, "r")
    roomlist = []
    linelist = []
    temproomformat = []

    for line in roomfile:
        linelist.append(line)

    while linelist[0] != "STOP":

        temproomformat = []

        for line in range(0, int(linelist[1])):
            temproomformat.append([])
            for tile in range(0, int(linelist[2])):
                temproomformat[-1].append(linelist[3+line][tile])

        roomlist.append(Room(linelist[0], int(linelist[1]), int(linelist[2]), temproomformat))

        for x in range(4+int(linelist[2])):
            del(linelist[0])

    return roomlist
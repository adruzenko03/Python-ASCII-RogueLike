class Room (object):

    def __init__(self, name, xl, yl, layout):
        self.name = str(name)
        self.xl = int(xl)
        self.yl = int(yl)
        self.layout = layout

def load_room_file(file):

    roomfile = open(file, "r")
    roomlist = []
    linelist = []

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
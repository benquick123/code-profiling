import os

def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer


def izvedi(ime_datoteke):
    '''
    Takes a name of the file that contains directions
    (STRING or STRING INT) and returns a list of
    touples containing (x, y and direction) touples, that are
    calculated using function premiki.


    :param ime_datoteke:
    :return container:
    '''
    with open(ime_datoteke, "r") as f:
        lines = f.read().splitlines()
    d = ""
    direction = "N"
    x = y = 0
    container = []
    container.append((x,y,direction))
    for line in lines:
        if line == "DESNO":
            d = "R"
        elif line == "LEVO":
            d = "L"
        elif line[:6] == "NAPREJ":
            d = int(line.split(" ")[1])
        x, y, direction = premik(d, x, y, direction)
        container.append((x, y, direction))
    return container


def opisi_stanje(x, y, direction):
    '''Takes x, y corrdinates and direction and changes
    direction to a caret notation, and returns a string formated
    in a (3 characters, right alined) x:(3 characters, left alined)y
    (space) caret with orientation.

    :param x:
    :param y:
    :param direction:
    :return a string containing x, y and direction:
    '''
    directions = "NESW"
    carets = "^>v<"
    return "{:>3}:{:<3} {}".format(x, y, carets[directions.index(direction)])

def prevedi(input_name, output_name):
    '''Takes the name of file to read from and to write too. Proceeds to write
    resutls of opisi_stanje() for each value in izvedi() to output_name.

    :param input_name:
    :param output_name:
    :return //:
    '''
    i = [opisi_stanje(x, y, direction) for x, y, direction in izvedi(input_name)]
    with open(output_name, "wt") as f:
        for item in i:
            f.write(item+"\n")

def opisi_stanje_2(x, y, direction):
    '''Takes x and y corrdinates and direction and changes
        direction to a caret notation, and returns a string formated
        in a caret with orientation (space) ((4 characters, right alined)
        x:(2 characters, left alined)y).

        :param x:
        :param y:
        :param direction:
        :return a string containing x, y and direction:
    '''
    directions = "NESW"
    carets = "^>v<"
    return "{} {:>4}:{:<2}".format(carets[directions.index(direction)], "("+str(x), str(y)+")")

def prevedi2(input_name, output_name):
    '''Takes the name of file to read from and to write too. Proceeds to write
        resutls of opisi_stanje2() for each value in izvedi() to output_name.

        :param input_name:
        :param output_name:
        :return //:
        '''
    i = [opisi_stanje_2(x, y, direction) for x, y, direction in izvedi(input_name)]
    with open(output_name, "w") as f:
        for item in i:
            f.write(item + "\n")







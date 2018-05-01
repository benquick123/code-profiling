###################################################### GIVEN FUNCTION ######################################################

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

###################################################### OBLIGATORY ASSIGNMENTS ######################################################

def izvedi(ime_datoteke):
    """
    Function gives back list of states that robot goes through while executing orders from a file.

    Args:
        file_of_orders: Name of a file that contains orders.

    Returns:
        list_of_states
    """
    moves = []
    datoteka = open(ime_datoteke)
    x = 0
    y = 0
    direction = "N"
    moves.append((x, y, direction))
    for element in datoteka:
        if element.strip() == "DESNO":
            x, y, direction = premik("R", x, y, direction)
            moves.append((x, y, direction))
        elif element.strip() == "LEVO":
            x, y, direction = premik("L", x, y, direction)
            moves.append((x, y, direction))
        else:
            nw_element = element.strip().split(" ")
            x, y, direction = premik(int(nw_element[1]), x, y, direction)
            moves.append((x, y, direction))
    datoteka.close()
    return moves

def opisi_stanje(x, y, smer):
    """
    Function gives back description of a state that robot is in.

    Args:
        x (int): Coordinate of a robot on a x axis.
        y (int): Coordinate of a robot on a y axis.
        smer (str): Direction of a robot.

    Returns:
        str: Description of a state.
    """
    if smer == "N":
        return "{:>3}:{:<3} ^".format(x, y)
    if smer == "E":
        return "{:>3}:{:<3} >".format(x, y)
    if smer == "S":
        return "{:>3}:{:<3} v".format(x, y)
    if smer == "W":
        return "{:>3}:{:<3} <".format(x, y)


def prevedi(ime_vhoda, ime_izhoda):
    """
    Function formats description of states and writes them in the new file.

    Args:
        ime_vhoda: Name of a file that contains orders.
        ime_izhoda: Name of a file that function will create.

    Returns:
        New file with orders.
    """
    moves = izvedi(ime_vhoda)
    exit_file = open(ime_izhoda, "w")
    for move in moves:
        states = opisi_stanje(move[0], move[1], move[2])
        exit_file.write("{}\n".format(states))
    exit_file.close()

###################################################### EXTRA ASSIGNMENT ######################################################

def opisi_stanje_2(x, y, smer):
    """
    Function gives back description of a state that robot is in.

    Args:
        x (int): Coordinate of a robot on a x axis.
        y (int): Coordinate of a robot on a y axis.
        smer (str): Direction of a robot.

    Returns:
        str: Description of a state.
    """
    if smer == "N":
        return "^ {:>4}:{:<}".format("({}".format(x), "{})".format(y))
    if smer == "E":
        return "> {:>4}:{:<}".format("({}".format(x), "{})".format(y))
    if smer == "S":
        return "v {:>4}:{:<}".format("({}".format(x), "{})".format(y))
    if smer == "W":
        return "< {:>4}:{:<}".format("({}".format(x), "{})".format(y))


###################################################### TESTS ######################################################


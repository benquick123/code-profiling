
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

def translate_command(command):
    translations = {"NAPREJ" : "N", "DESNO" : "R", "LEVO" : "L"}

    command_args = command.split(" ")
    value = translations[command_args[0]]  # This sets it for rotation change (DESNO, LEVO)

    # If the command is a movement command then set the movement as value
    if len(command_args) == 2:
        value = int(command_args[1])

    return value

def izvedi(ime_datoteke):
    file = open(ime_datoteke, "r")

    robot_current_state = (0, 0, 'N')
    robot_states = [robot_current_state]

    for line in file:
        line = line.rstrip()

        command = translate_command(line)
        x = robot_current_state[0]
        y = robot_current_state[1]
        direction = robot_current_state[2]

        robot_current_state = premik(command, x, y, direction)
        robot_states.append(robot_current_state)

    file.close()

    return robot_states

def opisi_stanje(x, y, smer):
    directions = {"N" : "^", "E" : ">", "S" : "v", "W" : "<"}
    direction = directions[smer]

    return "{:>3}:{:<3} {}".format(x, y, direction)

def prevedi(ime_vhoda, ime_izhoda):
    robot_states = izvedi(ime_vhoda)

    file = open(ime_izhoda, "w")

    for state in robot_states:
        translated_state = opisi_stanje(state[0], state[1], state[2])
        file.write(translated_state + "\n")

    file.close()

def opisi_stanje_2(x, y, smer):
    directions = {"N": "^", "E": ">", "S": "v", "W": "<"}
    direction = directions[smer]

    return "{}{:>5}:{})".format(direction, "(" + str(x), y)


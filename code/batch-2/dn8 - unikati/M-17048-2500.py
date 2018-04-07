
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

import unittest
class TestObvezna(unittest.TestCase):
    def test_branje(self):
        self.assertEqual(
            izvedi("primer.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (12, 0, 'E'), (12, 0, 'S'), (12, 2, 'S'),
             (12, 2, 'E'), (15, 2, 'E'), (15, 2, 'N'), (15, 2, 'W')]
        )
        self.assertEqual(
            izvedi("ukazi.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'), (1, 0, 'W'),
             (0, 0, 'W'), (0, 0, 'S'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'),
             (1, 3, 'S'), (1, 3, 'E'), (2, 3, 'E'), (2, 3, 'S'), (2, 3, 'W')]
        )

    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje(0, 12, "N"), "  0:12  ^")
        self.assertEqual(opisi_stanje(111, 0, "E"), "111:0   >")
        self.assertEqual(opisi_stanje(-2, 111, "S"), " -2:111 v")
        self.assertEqual(opisi_stanje(0, 0, "W"), "  0:0   <")

    def test_prevedi(self):
        from random import randint
        import os
        ime = "izhod{:05}.txt".format(randint(0, 99999))
        try:
            self.assertIsNone(prevedi("primer.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
 12:0   >
 12:0   v
 12:2   v
 12:2   >
 15:2   >
 15:2   ^
 15:2   <""")

            self.assertIsNone(prevedi("ukazi.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
  1:0   >
  1:0   v
  1:0   <
  0:0   <
  0:0   v
  0:0   >
  1:0   >
  1:0   v
  1:3   v
  1:3   >
  2:3   >
  2:3   v
  2:3   <""")
        finally:
            os.remove(ime)

        vime = "vhod{:05}.txt".format(randint(0, 99999))
        open(vime, "wt").write("NAPREJ 23\nLEVO\nNAPREJ 17\n")
        try:
            self.assertIsNone(prevedi(vime, ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:-23 ^
  0:-23 <
-17:-23 <""")
        finally:
            os.remove(ime)
            os.remove(vime)


class TestDodatna(unittest.TestCase):
    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje_2(0, 12, "N"),   "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"),  "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"),    "<   (0:0)")


if __name__ == "__main__":
    unittest.main()
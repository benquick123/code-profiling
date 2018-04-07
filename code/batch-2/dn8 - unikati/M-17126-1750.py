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

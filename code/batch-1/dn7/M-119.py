
from math import sqrt
import unittest

def sosedov(x, y, mine):
	return len([(x + xt, y + yt) for xt in range(-1, 2) for yt in range(-1, 2) if ((x + xt, y + yt) in mine) and (xt != 0 or yt != 0)])

import collections

def najvec_sosedov(mine, s, v):
	return collections.OrderedDict(sorted(({sosedov(xt, yt, mine): (xt, yt) for xt in range(s) for yt in range(v)}).items())).popitem()[1]

def brez_sosedov(mine, s, v):
	return set((xt, yt) for xt in range(s) for yt in range(v) if sosedov(xt, yt, mine) == 0)

def po_sosedih(mine, s, v):
	return {i: {(xt, yt)for xt in range(s) for yt in range(v) if sosedov(xt, yt, mine) == i} for i in range(9)}

def dolzina_poti(pot):
	return sum([sqrt((x1 - x0)**2 + (y1 - y0)**2) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
	return all((xt, yt) not in mine for xt in range(min(x0, x1), max(x0, x1) + 1) for yt in range(min(y0, y1), max(y0, y1) + 1))

def varna_pot(pot, mine):
	return (pot[0][0], pot[0][1]) not in mine if len(pot) == 1 else all(varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))


def polje_v_mine(polje):
	arr = set()
	i = 0
	for str in polje.split():
		for j in range(len(str)):
			if str[j] == 'X':
				arr.add((j, i))
		i += 1
	return (arr, len(str), len(polje.split()))

def preberi_pot(ukazi):
	pot = [(0, 0)]
	smer = 0
	switch = {0: lambda x, y, step: (x, y - step), #up
			  1: lambda x, y, step: (x + step, y), #left
			  2: lambda x, y, step: (x, y + step), #down
			  3: lambda x, y, step: (x - step, y)} #left
	for i in ukazi.split():
		if i == 'DESNO':
			smer = (smer + 1) % 4
		elif i == 'LEVO':
			smer = (smer - 1) % 4
			if smer < 0:
				smer = 3
		else:
			pot.append(switch[smer](pot[-1][0], pot[-1][1], int(i)))
	return pot

def zapisi_pot(ukazi):
	pot = ""
	smer = 0
	for i in range(len(ukazi) - 1):
		if ukazi[i][1] > ukazi[i+1][1]: #up
			pot += "DESNO " * (4 - smer) + str(ukazi[i][1] - ukazi[i+1][1]) + " "
			smer = 0
		elif ukazi[i][1] < ukazi[i+1][1]: #down
			pot +="DESNO " * (6 - smer) + str(ukazi[i+1][1] - ukazi[i][1]) + " "
			smer = 2
		elif ukazi[i][0] < ukazi[i+1][0]: #right
			pot +="DESNO " * (5 - smer) + str(ukazi[i+1][0] - ukazi[i][0]) + " "
			smer = 1
		elif ukazi[i][0]  > ukazi[i+1][0]: #left
			pot +="DESNO " * (7 - smer) + str(ukazi[i][0] - ukazi[i+1][0]) + " "
			smer = 3
	return pot


"""def zapisi_pot(ukazi):
	pot = ""
	smer = 0
	switch = {0: lambda smer, step: "DESNO " * (4 - smer) + str(step) + " ", #up
			  1: lambda smer, step: "DESNO " * (5 - smer) + str(step) + " ", #rigth
			  2: lambda smer, step: "DESNO " * (6 - smer) + str(step) + " ", #down
			  3: lambda smer, step: "DESNO " * (7 - smer) + str(step) + " ",} #left
	for i in range(len(ukazi) - 1):
		step = sqrt((ukazi[i+1][1] - ukazi[i][1]) ** 2 + (ukazi[i+1][0] - ukazi[i][0]) ** 2)
		if ukazi[i+1][0] > ukazi[i][0]:
			smer_temp = 1
		elif ukazi[i+1][0] < ukazi[i][0]:
			smer_temp = 3
		elif ukazi[i+1][1] > ukazi[i][1]:
			smer_temp = 2
		elif ukazi[i+1][1] < ukazi[i][1]:
			smer_temp = 0
		pot += switch[smer_temp](smer, int(step))
		smer = smer_temp 
	return pot"""


"""
...X....
.X....X.
.XX.....
......X.
"""
mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
s1, v1 = 8, 4


"""
........
........
........
"""
mine2 = set()
s2, v2 = 8, 3


"""
...X...X.X....X.
"""
mine3 = {(3, 0), (7, 0), (9, 0), (14, 0)}
s3, v3 = 16, 1

"""
X
"""
mine4 = {(0, 0)}
s4, v4 = 1, 1

"""
X
.
.
X
.
X
.
"""
mine5 = {(0, 0), (0, 3), (0, 5)}
s5, v5 = 1, 7

class Test06(unittest.TestCase):
		def test_01_sosedov(self):
				self.assertEqual(sosedov(2, 1, mine1), 4)
				self.assertEqual(sosedov(0, 3, mine1), 1)
				self.assertEqual(sosedov(4, 3, mine1), 0)
				self.assertEqual(sosedov(4, 2, mine1), 0)
				self.assertEqual(sosedov(0, 0, mine1), 1)
				self.assertEqual(sosedov(7, 0, mine1), 1)
				self.assertEqual(sosedov(3, 0, mine1), 0)

				self.assertEqual(sosedov(2, 2, mine2), 0)
				self.assertEqual(sosedov(0, 0, mine2), 0)
				self.assertEqual(sosedov(0, 0, mine2), 0)

				self.assertEqual(sosedov(0, 0, mine3), 0)
				self.assertEqual(sosedov(2, 0, mine3), 1)
				self.assertEqual(sosedov(3, 0, mine3), 0)
				self.assertEqual(sosedov(8, 0, mine3), 2)

				self.assertEqual(sosedov(0, 0, mine4), 0)

				self.assertEqual(sosedov(0, 0, mine5), 0)
				self.assertEqual(sosedov(0, 1, mine5), 1)
				self.assertEqual(sosedov(0, 2, mine5), 1)
				self.assertEqual(sosedov(0, 3, mine5), 0)
				self.assertEqual(sosedov(0, 4, mine5), 2)
				self.assertEqual(sosedov(0, 5, mine5), 0)
				self.assertEqual(sosedov(0, 6, mine5), 1)

		def test_02_najvec_sosedov(self):
				self.assertEqual(najvec_sosedov(mine1, s1, v1), (2, 1))
				x, y = najvec_sosedov(mine2, s2, v2)
				self.assertTrue(0 <= x < s2)
				self.assertTrue(0 <= y < v2)
				self.assertEqual(najvec_sosedov(mine3, s3, v3), (8, 0))
				self.assertEqual(najvec_sosedov(mine4, s4, v4), (0, 0))
				self.assertEqual(najvec_sosedov(mine5, s5, v5), (0, 4))

		def test_03_brez_sosedov(self):
				self.assertEqual(brez_sosedov(mine1, s1, v1),
												 {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)})
				self.assertEqual(brez_sosedov(mine2, s2, v2),
												 {(x, y) for x in range(s2) for y in range(v2)})
				self.assertEqual(brez_sosedov(mine3, s3, v3),
												 {(x, 0) for x in (0, 1, 3, 5, 7, 9, 11, 12, 14)})
				self.assertEqual(brez_sosedov(mine4, s4, v4), {(0, 0)})
				self.assertEqual(brez_sosedov(mine5, s5, v5),
												 {(0, 0), (0, 3), (0, 5)})

		def test_04_po_sosedih(self):
				self.assertEqual(po_sosedih(mine1, s1, v1),
												 {0: {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)},
													1: {(7, 3), (3, 2), (0, 0), (7, 0), (3, 3), (7, 1),
															(4, 0), (6, 0), (5, 0), (5, 3), (5, 1), (1, 0),
															(4, 1), (0, 3)},
													2: {(0, 1), (1, 2), (1, 3), (0, 2), (3, 1), (2, 0),
															(6, 2), (2, 3), (2, 2), (5, 2), (1, 1), (7, 2)},
													3: set(),
													4: {(2, 1)},
													5: set(),
													6: set(),
													7: set(),
													8: set()}
												 )

				prazen = dict.fromkeys(range(9), set())
				prazen[0] = {(x, y) for x in range(s2) for y in range(v2)}
				self.assertEqual(po_sosedih(mine2, s2, v2), prazen)

				s = dict.fromkeys(range(9), set())
				s.update({0: {(9, 0), (0, 0), (7, 0), (12, 0), (3, 0), (11, 0),
											(14, 0), (5, 0), (1, 0)},
									1: {(15, 0), (6, 0), (2, 0), (10, 0), (13, 0), (4, 0)},
									2: {(8, 0)}})
				self.assertEqual(po_sosedih(mine3, s3, v3), s)

				s = dict.fromkeys(range(9), set())
				s.update({0: {(9, 0), (0, 0), (7, 0), (12, 0), (3, 0), (11, 0),
											(14, 0), (5, 0), (1, 0)},
									1: {(15, 0), (6, 0), (2, 0), (10, 0), (13, 0), (4, 0)},
									2: {(8, 0)}})
				self.assertEqual(po_sosedih(mine3, s3, v3), s)

				s = dict.fromkeys(range(9), set())
				s[0] = {(0, 0)}
				self.assertEqual(po_sosedih(mine4, s4, v4), s)

				s = dict.fromkeys(range(9), set())
				s.update({0: {(0, 3), (0, 0), (0, 5)},
									1: {(0, 1), (0, 6), (0, 2)},
									2: {(0, 4)}})
				self.assertEqual(po_sosedih(mine5, s5, v5), s)


class Test07(unittest.TestCase):
		def test_01_dolzina_poti(self):
				self.assertEqual(dolzina_poti([(7, 2), (7, 5)]), 3)
				self.assertEqual(dolzina_poti([(7, 5), (7, 2)]), 3)
				self.assertEqual(dolzina_poti([(7, 5), (4, 5)]), 3)
				self.assertEqual(dolzina_poti([(1, 5), (4, 5)]), 3)
				self.assertEqual(
						dolzina_poti([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]),
						3 + 4 + 1 + 3 + 1)
				self.assertEqual(
						dolzina_poti([(0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]),
						4 + 1 + 3 + 1)
				self.assertEqual(
						dolzina_poti([(0, 0), (0, 1), (3, 1)]),
						1 + 3)
				self.assertEqual(dolzina_poti([(5, 3)]), 0)
				self.assertEqual(dolzina_poti([]), 0)

		"""
		...X....
		.X....X.
		.XX.....
		......X.
		"""
		def test_02_varen_premik(self):
				self.assertTrue(varen_premik(3, 1, 3, 3, mine1))
				self.assertTrue(varen_premik(3, 3, 3, 1, mine1))
				self.assertTrue(varen_premik(4, 0, 7, 0, mine1))
				self.assertTrue(varen_premik(7, 0, 4, 0, mine1))
				self.assertTrue(varen_premik(2, 1, 5, 1, mine1))
				self.assertTrue(varen_premik(5, 1, 2, 1, mine1))

				self.assertFalse(varen_premik(2, 1, 6, 1, mine1))
				self.assertFalse(varen_premik(6, 1, 2, 1, mine1))
				self.assertFalse(varen_premik(1, 1, 5, 1, mine1))
				self.assertFalse(varen_premik(5, 1, 1, 1, mine1))
				self.assertFalse(varen_premik(0, 1, 4, 1, mine1))
				self.assertFalse(varen_premik(4, 1, 0, 1, mine1))

				self.assertFalse(varen_premik(2, 1, 2, 3, mine1))
				self.assertFalse(varen_premik(2, 3, 2, 1, mine1))
				self.assertFalse(varen_premik(2, 1, 2, 2, mine1))
				self.assertFalse(varen_premik(2, 2, 2, 1, mine1))
				self.assertFalse(varen_premik(2, 2, 2, 0, mine1))
				self.assertFalse(varen_premik(2, 0, 2, 2, mine1))

				self.assertFalse(varen_premik(1, 1, 1, 1, mine1))

		"""
		...X....
		.X....X.
		.XX.....
		......X.
		"""
		def test_03_varna_pot(self):
				self.assertTrue(varna_pot([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
				self.assertTrue(varna_pot([(0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
				self.assertTrue(varna_pot([(2, 1)], mine1))
				self.assertTrue(varna_pot([], mine1))

				self.assertFalse(varna_pot([(0, 0), (0, 1), (3, 1)], mine1))
				self.assertFalse(varna_pot([(0, 0), (1, 0), (1, 3)], mine1))
				self.assertFalse(varna_pot([(0, 0), (1, 0), (0, 0), (1, 0), (1, 3), (3, 3)], mine1))
				self.assertFalse(varna_pot([(1, 1)], mine1))


class Test08(unittest.TestCase):
		def test_01_polje_v_mine(self):
				# Če si sledi več nizov, med katerimi ni ničesar, jih Python zlepi
				# ".X. "   "..X" je isto kot ".X. ...".
				self.assertEqual(polje_v_mine("...X.... "
																			".X....X. "
																			".XX..... "
																			"......X."), (mine1, s1, v1))
				self.assertEqual(polje_v_mine("........ "
																			"........ "
																			"........"), (mine2, s2, v2))
				self.assertEqual(polje_v_mine("...X...X.X....X."), (mine3, s3, v3))
				self.assertEqual(polje_v_mine("X"), (mine4, s4, v4))
				self.assertEqual(polje_v_mine("X "
																			". "
																			". "
																			"X "
																			". "
																			"X "
																			". "), (mine5, s5, v5))


class Test10(unittest.TestCase):
		def test_01_preberi_pot(self):
				self.assertEqual(
						preberi_pot(
"""DESNO
DESNO
3
LEVO
4
LEVO
1
DESNO
3
DESNO
1"""), [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)])

				self.assertEqual(
						preberi_pot(
"""DESNO
LEVO
DESNO
DESNO
DESNO
DESNO
DESNO
3"""), [(0, 0), (3, 0)])

				self.assertEqual(
						preberi_pot(
"""LEVO
DESNO
LEVO
LEVO
LEVO
LEVO
DESNO
3"""), [(0, 0), (3, 0)])

				self.assertEqual(
						preberi_pot(
"""LEVO
DESNO
LEVO
LEVO
LEVO
LEVO
DESNO
3"""), [(0, 0), (3, 0)])

				self.assertEqual(
						preberi_pot(
"""DESNO
3
DESNO
3
DESNO
3
DESNO
3"""), [(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])

				self.assertEqual(
						preberi_pot(
"""DESNO
1
DESNO
DESNO
1
LEVO
LEVO
1
DESNO
3
LEVO
2
DESNO
DESNO"""), [(0, 0), (1, 0), (0, 0), (1, 0), (1, 3), (3, 3)])

		def test_02_zapisi_pot(self):
				pot = [(0, 0), (3, 0)]
				self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

				pot = [(0, 0), (3, 0), (3, 3)]
				self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

				pot = [(0, 0), (3, 0), (3, 3), (3, 5), (5, 5), (5, 1), (4, 1), (6, 1), (6, 8), (6, 3)]
				self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

				pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
				self.assertEqual(preberi_pot(zapisi_pot(pot)), pot)

if __name__ == "__main__":
		unittest.main()

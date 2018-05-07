def capitalize(xs):
    list = []
    for x in xs:
        list.append(x.capitalize())
    return list

def icapitalize(xs):
    x = 0
    while x < len(xs):
        xs[x] = xs[x].capitalize()
        x +=1


def count(n):
    rez = 10
    while rez > 9:
        rez = 0
        for i in str(n):
            rez += int(i)
        n = rez
    return n

def postnina(n):
    list = []
    for a in range(1, int(n**(1. / 3))+1):
        for b in range(1, int((n//a)**(1./2))+1):
            c = (n//a)//b
            if a*b*c == n:
                list.append(a+b+c)
    return min(list)

def nic_ena(xs):
    a = xs.count(0)
    b = xs.count(1)
    list = []
    for n in range(a):
        list.append(0)
    for n in range(b):
        list.append(1)
    return sum(i != j for i, j in zip(xs, list))





import unittest

class TestNaloge8(unittest.TestCase):
    def test_capitalize(self):
        imena = ['marko', 'Miha', 'maja', 'Monika']
        self.assertEqual(capitalize(imena), ['Marko', 'Miha', 'Maja', 'Monika'])
        self.assertEqual(imena, ['marko', 'Miha', 'maja', 'Monika'])

        imena = ['ana', 'anja', 'alen', 'aljana', 'angelika']
        self.assertEqual(capitalize(imena), ['Ana', 'Anja', 'Alen', 'Aljana', 'Angelika'])
        self.assertEqual(imena, ['ana', 'anja', 'alen', 'aljana', 'angelika'])

    def test_icapitalize(self):
        imena = ['marko', 'Miha', 'maja', 'Monika']
        self.assertIsNone(icapitalize(imena))
        self.assertEqual(imena, ['Marko', 'Miha', 'Maja', 'Monika'])

        imena = ['ana', 'anja', 'alen', 'aljana', 'angelika']
        self.assertIsNone(icapitalize(imena))
        self.assertEqual(imena, ['Ana', 'Anja', 'Alen', 'Aljana', 'Angelika'])

    def test_count(self):
        self.assertEqual(count(1), 1)
        self.assertEqual(count(23), 5)
        self.assertEqual(count(12345), 6)
        self.assertEqual(count(999999999), 9)
        self.assertEqual(count(213413512), 4)
        self.assertEqual(count(2147483647), 1)
        self.assertEqual(count(21499999997483999999964999919997), 2)

    def test_postnina(self):
        self.assertEqual(postnina(1), 3)
        self.assertEqual(postnina(6), 6)
        self.assertEqual(postnina(7), 9)
        self.assertEqual(postnina(10), 8)
        self.assertEqual(postnina(100), 14)
        self.assertEqual(postnina(200), 18)
        self.assertEqual(postnina(300), 21)

    def test_nic_ena(self):
        self.assertEqual(nic_ena([0, 0, 1, 0, 1]), 1)
        self.assertEqual(nic_ena([0, 0, 1, 1, 1]), 0)
        self.assertEqual(nic_ena([0, 1, 0, 1, 0]), 2)
        self.assertEqual(nic_ena([1, 1, 1, 1, 0, 0, 0]), 3)
        self.assertEqual(nic_ena([1, 0, 0, 0, 1, 1, 1, 0]), 2)
        self.assertEqual(nic_ena([0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]), 6)
        self.assertEqual(nic_ena([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]), 9)
        self.assertEqual(nic_ena([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 10)

    def test_mask(self):
        self.assertCountEqual(mask(0), [[]])
        self.assertCountEqual(mask(1), [[0], [1]])
        self.assertCountEqual(mask(2), [[0, 0], [0, 1], [1, 0], [1, 1]])
        self.assertCountEqual(mask(3), [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
        self.assertEqual(len(mask(10)), 1024)
        self.assertEqual(len(mask(16)), 65536)

    def test_potencna(self):
        self.assertCountEqual(potencna([]), [[]])
        self.assertCountEqual(potencna([1, 5]), [[], [1], [5], [1, 5]])
        self.assertCountEqual(potencna([1, 5, 7]), [[], [1], [5], [1, 5], [7], [1, 7], [5, 7], [1, 5, 7]])
        self.assertEqual(len(potencna(list(range(10)))), 1024)

    def test_knjige(self):
        self.assertTrue(knjige([10, 20, 30]))
        self.assertTrue(knjige([10, 20, 30, 40]))
        self.assertTrue(knjige([11, 20, 12, 42, 20, 20, 11, 20, 20, 20, 4]))
        self.assertTrue(knjige([23, 51, 51, 153, 20, 25, 51, 59, 39, 35, 91]))
        self.assertTrue(knjige([33, 9, 15, 14, 7, 35, 13, 8, 38, 10, 60, 14, 12, 56]))
        self.assertTrue(knjige([101, 42, 132, 41, 120, 301, 401, 180, 150, 11, 11]))

        self.assertFalse(knjige([10, 20, 30, 40, 50]))
        self.assertFalse(knjige([11, 20, 12, 42, 22, 20, 11, 20, 20, 20, 4]))
        self.assertFalse(knjige([23, 51, 51, 153, 25, 51, 59, 39, 35, 91]))
        self.assertFalse(knjige([101, 42, 132, 41, 120, 301, 401, 180]))


if __name__ == '__main__':
    unittest.main(verbosity=2)

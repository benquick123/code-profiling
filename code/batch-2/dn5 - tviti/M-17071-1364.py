def unikati(s):
    list = []
    for x in s:
        if x not in list:
            list.append(x)
    return list

def avtor(tvit):
    x = tvit.split(":")
    return(x[0])

def vsi_avtorji(tviti):
    authors = []
    for x in tviti:
        splitx = x.split(":")
        if splitx[0] not in authors:
            authors.append(splitx[0])
    return authors

def izloci_besedo(beseda):
    temp = beseda
    while not temp[0].isalnum():
        temp = temp.replace(temp[0], "")
    while not temp[-1].isalnum():
        temp = temp.replace(temp[-1], "")
    return temp

def se_zacne_z(tvit, c):
    response = []
    temp_words = tvit.split(" ")
    for word in temp_words:
        if word[0] == c:
            temp = word
            while not temp[0].isalnum():
                temp = temp.replace(temp[0], "")
            while not temp[-1].isalnum():
                temp = temp.replace(temp[-1], "")
            response.append(temp)
    return response

def zberi_se_zacne_z(tviti, c):
    response = []
    for tvit in tviti:
        temp_words = tvit.split(" ")
        for word in temp_words:
            if word[0] == c:
                temp = word
                while not temp[0].isalnum():
                    temp = temp.replace(temp[0], "")
                while not temp[-1].isalnum():
                    temp = temp.replace(temp[-1], "")
                if temp not in response:
                    response.append(temp)
    return response

def vse_afne(tviti):
    response = []
    for tvit in tviti:
        x = tvit.split(" ")
        for word in x:
            if word[0] == "@":
                temp = ""
                for [letter] in word:
                    if letter.isalnum():
                        temp += letter
                if temp not in response:
                    response.append(temp)
    return response

def vsi_hashtagi(tviti):
    response = []
    for tvit in tviti:
        x = tvit.split(" ")
        for word in x:
            if word[0] == "#":
                temp = ""
                for [letter] in word:
                    if letter.isalnum():
                        temp += letter
                if temp not in response:
                    response.append(temp)
    return response

def vse_osebe(tviti):
    people = []
    for tvit in tviti:
        tvit_temp = tvit.split(":")
        if tvit_temp[0] not in people:
            people.append(tvit_temp[0])
        tvit_temp = tvit.split(" ")
        for word in tvit_temp:
            if word[0] == "@":
                temp = ""
                for [letter] in word:
                    if letter.isalnum():
                        temp += letter
                if temp not in people:
                    people.append(temp)
    speople = sorted(people)
    return speople

def custva(tviti, hastagi):
    hashtags = []
    response = []
    for tvit in tviti:
        temp_tvit = tvit.split(":")
        author = temp_tvit[0]
        temp_tvit = tvit.split(" ")
        for word in temp_tvit:
            if word[0] == "#":
                hashtags.append((author, word[1:]))
    for aut, feeling in hashtags:
        for x in hastagi:
            if feeling ==x:
                if aut not in response:
                    response.append(aut)
        response = sorted(response)
    return response

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        temp_tvit = tvit. split(":")
        coseba1 = temp_tvit[0]
        if oseba1 == coseba1:
            temp_tvit = tvit.split(" ")
            for word in temp_tvit:
                if word[0] == "@":
                    temp = word
                    while not temp[0].isalnum():
                        temp = temp.replace(temp[0], "")
                    while not temp[-1].isalnum():
                        temp = temp.replace(temp[-1], "")
                    if temp == oseba2:
                        return True
    else:
        return False



import unittest


class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_unikat(self):
        self.assertEqual(unikati([1, 2, 1, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(unikati([1, 3, 2, 1, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(unikati([1, 5, 4, 3, 2]), [1, 5, 4, 3, 2])
        self.assertEqual(unikati([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unikati([1]), [1])
        self.assertEqual(unikati([]), [])
        self.assertEqual(unikati(["Ana", "Berta", "Cilka", "Berta"]), ["Ana", "Berta", "Cilka"])

    def test_avtor(self):
        self.assertEqual(avtor("janez: pred dvopičjem avtor, potem besedilo"), "janez")
        self.assertEqual(avtor("ana: malo krajse ime"), "ana")
        self.assertEqual(avtor("benjamin: pomembne so tri stvari: prva, druga in tretja"), "benjamin")

    def test_vsi_avtorji(self):
        self.assertEqual(vsi_avtorji(self.tviti), ["sandra", "berta", "ana", "cilka", "benjamin", "ema"])
        self.assertEqual(vsi_avtorji(self.tviti[:3]), ["sandra", "berta"])

    def test_izloci_besedo(self):
        self.assertEqual(izloci_besedo("@ana"), "ana")
        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")
        self.assertEqual(izloci_besedo("ana"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")

    def test_vse_na_crko(self):
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])

    def test_zberi_na_crko(self):
        self.assertEqual(zberi_se_zacne_z(self.tviti, "@"), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_osebe(self):
        self.assertEqual(vse_osebe(self.tviti), ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'])


class TestDodatna(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_custva(self):
        self.assertEqual(custva(self.tviti, ["dougcajt", "krneki"]), ["ana", "sandra"])
        self.assertEqual(custva(self.tviti, ["luft"]), ["cilka"])
        self.assertEqual(custva(self.tviti, ["meh"]), [])

    def test_se_poznata(self):
        self.assertTrue(se_poznata(self.tviti, "ana", "berta"))
        self.assertTrue(se_poznata(self.tviti, "ema", "ana"))
        self.assertFalse(se_poznata(self.tviti, "sandra", "ana"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "luft"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "balon"))


if __name__ == "__main__":
    unittest.main()


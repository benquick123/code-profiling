######## obvezne funkcije ########


def unikati(s):
    new = []
    for e in s:
        if e not in new:
            new.append(e)
    return new


def avtor(tweet):
    temp = tweet.split(":")
    result = temp[0]
    return result


def vsi_avtorji(tweets):
    avtorji = []
    for tweet in tweets:
        a = avtor(tweet)
        if a not in avtorji:
            avtorji.append(a)
    return avtorji


def izloci_besedo(beseda):
    a = ""
    i = 0
    for b in beseda:
        if b.isalnum() == False:
            i += 1
        else:
            a = beseda[i:]
            break
    i = 0
    for b in a[::-1]:
        if b.isalnum() == False:
            i += 1
        else:
            if i == 0:
                break
            else:
                a = a[:-i]
                break
    return a


def se_zacne_z(tweet, c):
    temp = []
    result = []
    t = tweet.split()
    for word in t:
        if word.startswith(c):
            temp.append(word)
    for word in temp:
        x = izloci_besedo(word)
        result.append(x)
    return result


def zberi_se_zacne_z(tweets, c):
    temp = []
    for tweet in tweets:
        a = se_zacne_z(tweet, c)
        for w in a:
            if a != []:
                if w not in temp:
                    temp.append(w)
    temp = list(temp)
    return temp


def vse_afne(tweets):
    return zberi_se_zacne_z(tweets, "@")


def vsi_hashtagi(tweets):
    return zberi_se_zacne_z(tweets, "#")


def vse_osebe(tweets):
    a = zberi_se_zacne_z(tweets, "@")
    for tweet in tweets:
        temp = tweet.split()
        temp_char = izloci_besedo(temp[0])
        if temp_char not in a:
            a.append(temp_char)
    result = sorted(a)
    return result


###### END obvezne funkcije ######


######## dodatne funkcije ########

def custva(tweets, hashtags):
    a = []
    for tweet in tweets:
        for hash in hashtags:
            if hash in tweet:
                temp = tweet.split()
                temp_char = izloci_besedo(temp[0])
                if temp_char not in a:
                    a.append(temp_char)
                    break
                else:
                    break
    result = sorted(a)
    return result

def se_poznata(tweets, oseba1, oseba2):
    mentions = []
    for tweet in tweets:
        temp = tweet.split()
        author = izloci_besedo(temp[0])
        mention = zberi_se_zacne_z(temp, "@")
        for person in mention:
            s = izloci_besedo(person)
            mentions.append(s)
        if author == oseba1 and oseba2 in mentions:
            return True
        mentions = []
    return False



###### END dodatne funkcije ######


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


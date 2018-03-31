import unittest

def unikati(s):
    unique_list = []
    for element in s:
        found = False
        i = 0
        while i < len(unique_list) and not found:
            if unique_list[i] == element:
                found = True
            i += 1

        if not found:
            unique_list.append(element)

    return unique_list

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    authors = []
    for tweet in tviti:
        authors.append(avtor(tweet))

    return unikati(authors)

def izloci_besedo(beseda):
    start = 0
    for char in beseda:
        if char.isalnum():
            break
        start += 1

    end = len(beseda)
    for char in reversed(beseda):
        if char.isalnum():
            break
        end -= 1

    return beseda[start:end]

def se_zacne_z(tvit, c):
    searched_words = []
    words = tvit.split(" ")
    for word in words:
        if word[0] == c:
            searched_words.append(izloci_besedo(word))

    return searched_words

def zberi_se_zacne_z(tviti, c):
    searched_words = []
    for tweet in tviti:
        words_of_intrest = se_zacne_z(tweet, c)
        for word in words_of_intrest:
            searched_words.append(word)

    return unikati(searched_words)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    all_persons = []
    for tweet in tviti:
        author = tweet.split(":")[0]
        all_persons.append(author)

    for mentioned_person in vse_afne(tviti):
        all_persons.append(mentioned_person)

    all_persons = unikati(all_persons)

    return sorted(all_persons)

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

def custva(tviti, hashtagi):
    searched_persons = []
    for tweet in tviti:
        person = tweet.split(":")[0]
        persons_hashtags = se_zacne_z(tweet, '#')
        for hashtag in persons_hashtags:
            if hashtag in hashtagi:
                searched_persons.append(person)

    searched_persons = unikati(searched_persons)

    return sorted(searched_persons)

def get_tweets(person, tweets):
    persons_tweets = []
    for tweet in tweets:
        if tweet.split(":")[0] == person:
            persons_tweets.append(tweet)

    return persons_tweets

def se_poznata(tviti, oseba1, oseba2):
    persons1_tweets = get_tweets(oseba1, tviti)
    persons2_tweets = get_tweets(oseba2, tviti)

    for tweet in persons1_tweets:
        mentioned_persons = se_zacne_z(tweet, '@')
        for person in mentioned_persons:
            if person == oseba2:
                return True

    for tweet in persons2_tweets:
        mentioned_persons = se_zacne_z(tweet, '@')
        for person in mentioned_persons:
            if person == oseba1:
                return True

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


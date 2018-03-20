import unittest

############################################# OBLIGATORY ASSIGNMENT #############################################

### Function takes list and gives us cleaned list where each element appears only once.
def unikati(s):

    ### We create new empty list that we will return.
    cleaned_list = []
    for element in s:

        ### We inspect each element in the given list. If there is no same element already in the new list.
        if element not in cleaned_list:
            cleaned_list.append(element)

    ### We return newly created list.
    return cleaned_list

### Function gives us the author of the tweet that we input.
def avtor(tvit):

    ### As in the structure of tweet author stands before ":" we divide tweet on two parts and select ":" as division element.
    new_tvit = tvit.split(':')

    ### We return the first element that was standing before ":", that is author.
    return new_tvit[0]

### Function gives us list of all the authors of the selected tweets.
def vsi_avtorji(tviti):

    ### We create new empty list that we will return.
    authors = []

    ### For each element, that represents each tweet we call already created function "avtor" that gives us name of the author.
    for element in tviti:
        authors.append(avtor(element))

    ### We remove repeated authors from the list with already created function "unikati".
    return unikati(authors)

### Function cleans the words in tweets from all non alphanumerical elements at the start and end of word.
def izloci_besedo(beseda):

    ### While first element of the word is not alphanumerical element, we cut out that first element and start a word at the next element.
    while beseda[0].isalnum() == False:
        beseda = beseda[1:]

    ### We reverse word and repeat the cleaning with while loop.
    reversed_beseda = beseda[::-1]
    while reversed_beseda[0].isalnum() == False:
        reversed_beseda = reversed_beseda[1:]

    ### We reverse word again to get to the starting order and return the result of cleaning.
    beseda = reversed_beseda[::-1]
    return beseda

### Function gives us back list of the words from selected tweet that are starting with the selected element.
def se_zacne_z(tvit, c):

    ### We crate new empty list that we will return.
    startingwith_c_words = []

    ### We split element of a string to elements of the worlds, that will help us identify words that start with selected element.
    new_tvit = tvit.split(" ")

    ### We check first element of each word in the selected tweet.
    for word in new_tvit:

        ### If first element of the word is the same as selected element of criteria, we clean the word with function "izloci_besedo" and append it into newly created list.
        if word[0] == c:
            startingwith_c_words.append(izloci_besedo(word))
    return startingwith_c_words

### Function gives us back list of the words from selected tweets that are starting with the selected element.
def zberi_se_zacne_z(tviti, c):

    ### We crate new empty list that we will return.
    startingwith_c_words = []

    ### On each element (tweet) in selected list of tweets we apply created function "se_zacne_z" to get the words that start with selected element and append them to newly created list.
    for element in tviti:
        startingwith_c_words_single_tweet = se_zacne_z(element, c)
        for word in startingwith_c_words_single_tweet:
            startingwith_c_words.append(word)

    ### Before returning the newly created list we clean it of replicates with crated function "unikati".
    return unikati(startingwith_c_words)

### Function gives us all the words that start with "@".
def vse_afne(tviti):

    ### We use function "zberi_se_zacne_z" where we predefine second input element as "@".
    return zberi_se_zacne_z(tviti, "@")

### Function gives us all the words that start with "#".
def vsi_hashtagi(tviti):

    ### We use function "zberi_se_zacne_z" where we predefine second input element as "#".
    return zberi_se_zacne_z(tviti, "#")

### Function gives us the names of all the persons that are appearing in tweets.
def vse_osebe(tviti):

    ### We crate new empty list that we will return.
    persons = []

    ### We use function "vsi_avtorji" to get the list of all the authors (that are persons) appearing in the tweet as creators of tweet and by this append them in the newly created list.
    authors = vsi_avtorji(tviti)
    for author in authors:
        persons.append(author)

    ### We use function "vse_afne" to get the list of all the persons that are mentioned in the tweets and append them into newly created list.
    afne = vse_afne(tviti)
    for afna in afne:
        persons.append(afna)

    ### Before we return created list we clean it of replicates and sort names alphabetically.
    return sorted(unikati(persons))



############################################# EXTRA ASSIGNMENT #############################################


### Function gives us the list of authors who used selected hashtags in the givel list of tweets.
def custva(tviti, hashtagi):

    ### We crate new empty list that we will return.
    authors = []

    ### If selected hashtag appears in the tweet, we append it into newly created list.
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                authors.append(avtor(tvit))

    ### Before we return created list we clean it of replicates and sort names alphabetically.
    return sorted(unikati(authors))

### Funtion gives us list of people who appear in one tweet.
def people_in_tvit(tvit):

    ### We crate new empty list that we will return.
    people = []

    ### We append all the authors in the newly created list with already created function "avtor".
    author = avtor(tvit)
    people.append(author)

    ### If tweet contains "@" which indicates mentioned person, we call already created function "se_zacne_z" that gives us back list of names of mentioned persons.
    if "@" in tvit:
        mentioned_people = se_zacne_z(tvit, "@")

        ### We append every persons in the list to newly created list of all the people in the tweet.
        for name in mentioned_people:
            people.append(name)

    ### Before we return created list we clean it of replicates and sort names alphabetically.
    return sorted(unikati(people))

### Function checks if two authors know each other.
def se_poznata(tviti, oseba1, oseba2):

    ### For every tweet we call crated function "people in tweet" that gives us back list of all the people in tweet.
    for tvit in tviti:
        names_in_tvit = people_in_tvit(tvit)

        ### If both persons appear in the list, that means they know each other and we will get True.
        if oseba1 in names_in_tvit and oseba2 in names_in_tvit:
            return True

    ### If loop does not return True, that means, that persons don't know each other and function has to return False.
    return False



############################################# TESTS #############################################



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


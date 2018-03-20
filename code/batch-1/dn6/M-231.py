import unittest


############################################# OBLIGATORY ASSIGNMENT #############################################

### Function gives us the text of the tweet that we input. (01. TASK)
def besedilo(tvit):

    ### As in the structure of tweet author stands before ":" we divide tweet on two parts and select first ": " as division element.
    new_tvit = tvit.split(': ', 1)

    ### We return the second element that was standing after ": ", that is text of a tweet.
    return new_tvit[1]


### Function gives us the author of the tweet that we input.
def avtor(tvit):

    ### As in the structure of tweet author stands before ":" we divide tweet on two parts and select ":" as division element.
    new_tvit = tvit.split(':')

    ### We return the first element that was standing before ":", that is author.
    return new_tvit[0]


### Function gives us dictionary that consists authors as key to the tweets as values. Tweets are always the last ones that author tweeted. (02. TASK)
def zadnji_tvit(tviti):

    ### We create new empty dictionary that function will return.
    dic_tvit = {}

    ### For every tweet we use created functions "avtor" and "besedilo" that extract author and text from the tweet. Then we assign them place in the dictionary.
    for tvit in tviti:
        author = avtor(tvit)
        text = besedilo(tvit)
        dic_tvit[author] = text
    return dic_tvit


### Function gives us dictionary that consists authors as key to the tweets as values. Tweets are always the first ones that author tweeted. (03. TASK)
def prvi_tvit(tviti):

    ### We create new empty dictionary that function will return.
    dic_tvit = {}

    ### For every tweet we use created functions "avtor" and "besedilo" that extract author and text from the tweet.
    for tvit in tviti:
        author = avtor(tvit)
        text = besedilo(tvit)

        ### If the author is already in the dictionary as the key, we don't assign him new value.
        if author not in dic_tvit:
            dic_tvit[author] = text
    return dic_tvit


### Function gives us number of tweets that selected author has made.
def n_tvit(tviti, author):

    ### We set the starting point of counting to 0.
    count_tvit = 0

    ### For every tweet we extract the the author and check if the author is the same as the one twe have selected. If so, we add value of 1 to our counting variable and return it after loop finishes its work.
    for tvit in tviti:
        tvit_author = avtor(tvit)
        if author == tvit_author:
            count_tvit += 1
    return count_tvit


### Function gives us dictionary that consists authors as key to the number of tweets as values. (04. TASK)
def prestej_tvite(tviti):

    ### We create new empty dictionary that function will return.
    dic_n_tviti = {}

    ### For every tweet we use created functions "avtor" and "n_author" that extract author and number of tweets that same author has made. Then we assign them place in the dictionary.
    for tvit in tviti:
        author = avtor(tvit)
        n_author = n_tvit(tviti, author)
        dic_n_tviti[author] = n_author
    return dic_n_tviti



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


### Function gives us dictionary that consists authors as key to the people that these authors are mentioning as values. (05. TASK)
def omembe(tviti):

    ### We create new empty dictionary that function will return.
    dic_mentions = {}

    ### For every tweet we extract the author and mentioned persons by caling created functions " avtor" and "se_zacne_z".
    for tvit in tviti:
        author = avtor(tvit)
        mentioned = se_zacne_z(tvit, "@")

        ### If author is already in the dictionary we just add mentioned persons as another/extra value; otherwise we assign author as the new key and add him mentioned persons as values.
        if author in dic_mentions:
            dic_mentions[author] += mentioned
        else:
            dic_mentions[author] = mentioned
    return dic_mentions


### Function gives us a list of people who are authors of some tweets in the list, but are not mentioned in a tweets of selected author. (06. TASK)
def neomembe(ime, omembe):

    ### We create new empty list that function will return.
    not_mentioned = []

    ### For each person (except selected author) in dictionary of mentions we first check if she was mentioned by selected author. If she was not mentioned, we append it to created list.
    for author in omembe:
        if author != ime:
            if author not in omembe[ime]:
                not_mentioned.append(author)
    return not_mentioned


############################################# EXTRA ASSIGNMENT #############################################

### Function tells us if one or other selected author ever mentioned other author in its tweet. (01. TASK)
def se_poznata(ime1, ime2, omembe):

    ### First we check if which of the selected persons if key and then we check if the other person appear as value under under this key. If it does we return "True" otherwise we return "False".
    for names in omembe:
        if ime1 == names:
            if ime2 in omembe[ime1]:
                return True
        elif ime2 == names:
            if ime1 in omembe[ime2]:
                return True
    return False

############################################# IMPORTED FUNCTIONS FOR LAST TASK #############################################

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


### Function gives us all the words that start with "#".
def vsi_hashtagi(tviti):

    ### We use function "zberi_se_zacne_z" where we predefine second input element as "#".
    return zberi_se_zacne_z(tviti, "#")

###########################################################################################################################

def hashtagi(tviti):

    ### We crate new empty dictionary and extract all the hashtags from list given tweets by calling function "vsi_hashtagi".
    dic_hashtagi = {}
    list_of_hashtags = vsi_hashtagi(tviti)

    ### For each tweet we extract author by calling created function "avtor".
    for tvit2 in tviti:
        author = avtor(tvit2)
        for hashtag in list_of_hashtags:

            ### If specific hashtag appears in the same tweet as specific author we add this information to dictionary. If in dictionary key of specific hashtag already exist, we just add new value under it.
            if hashtag in tvit2 and author in tvit2:
                if hashtag in dic_hashtagi:
                    dic_hashtagi[hashtag] += [author]
                else:
                    dic_hashtagi[hashtag] = [author]

    ### We sort values under all keys and return new dictionary.
    for hashtags in dic_hashtagi:
        dic_hashtagi[hashtags] = sorted(dic_hashtagi[hashtags])
    return dic_hashtagi


############################################# TESTS #############################################


class TestObvezna(unittest.TestCase):
    maxDiff = 10000

    def test_1_besedilo(self):
        self.assertEqual(besedilo("sandra: Spet ta dež. #dougcajt"),
                         "Spet ta dež. #dougcajt")
        self.assertEqual(besedilo("ana: kdo so te: @berta, @cilka, @dani? #krneki"),
                         "kdo so te: @berta, @cilka, @dani? #krneki")

    def test_2_zadnji_tvit(self):
        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"berta": "@sandra Delaj domačo za #programiranje1",
             "sandra": "@berta Ne maram #programiranje1 #krneki",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "cilka": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "sandra": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(zadnji_tvit([]), {})


    def test_3_prvi_tvit(self):
        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "berta": "@sandra Delaj domačo za #programiranje1",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "cilka": "jst sm pa #luft",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(prvi_tvit([]), {})

    def test_4_prestej_tvite(self):
        self.assertDictEqual(
            prestej_tvite([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 2, "berta": 1, "ana": 1, "cilka": 2, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite([
                    "sandra: Spet ta dež. #dougcajt",
                    "sandra: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "sandra: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 5, "ana": 1, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": 1})

        self.assertEqual(prestej_tvite([]), {})

    def test_5_omembe(self):
        self.assertDictEqual(
            omembe(["sandra: Spet ta dež. #dougcajt",
                    "berta: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "cilka: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": ["berta", "benjamin", "ana"],
             "benjamin": [],
             "cilka": [],
             "berta": ["sandra"],
             "ana": ["berta", "cilka", "dani"]}
        )

    def test_6_neomembe(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani", "benjamin", "sandra"]}

        self.assertEqual(neomembe("sandra", omembe), ["cilka"])
        self.assertEqual(neomembe("ana", omembe), [])
        self.assertEqual(set(neomembe("benjamin", omembe)), set(omembe) - {"benjamin"})

class TestDodatna(unittest.TestCase):
    def test_1_se_poznata(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani"]}

        self.assertTrue(se_poznata("ana", "berta", omembe))
        self.assertTrue(se_poznata("berta", "ana", omembe))
        self.assertTrue(se_poznata("sandra", "benjamin", omembe))
        self.assertTrue(se_poznata("benjamin", "sandra", omembe))

        self.assertFalse(se_poznata("benjamin", "ana", omembe))
        self.assertFalse(se_poznata("ana", "benjamin", omembe))

        self.assertFalse(se_poznata("cilka", "dani", omembe))
        self.assertFalse(se_poznata("pavel", "peter", omembe))

    def test_2_hashtagi(self):
        self.assertDictEqual(
            hashtagi(["sandra: Spet ta dež. #dougcajt",
                      "berta: @sandra Delaj domačo za #programiranje1",
                      "sandra: @berta Ne maram #programiranje1 #krneki",
                      "ana: kdo so te @berta, @cilka, @dani? #krneki",
                      "cilka: jst sm pa #luft",
                      "benjamin: pogrešam ano #zalosten",
                      "ema: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {'dougcajt': ['sandra'],
             'krneki': ['ana', 'sandra'],
             'luft': ['cilka'],
             'programiranje1': ['berta', 'sandra'],
             'split': ['ema'],
             'zalosten': ['benjamin']})


if __name__ == "__main__":
    unittest.main()



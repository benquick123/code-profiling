### funkcije iz prejsnje naloge ###
def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda


######### naloga #########

###### obvezni del ######

def besedilo(tweet):
    a = tweet.split(": ", 1)
    return " ".join(a[1:])


def zadnji_tvit(tweets):
    result = {}
    for tweet in tweets:
        entry = besedilo(tweet)
        key = tweet.split(":")[0]
        result[key] = entry
    return result


def prvi_tvit(tweets):
    result = {}
    for tweet in tweets:
        entry = besedilo(tweet)
        key = tweet.split(":")[0]
        if key not in result:
            result[key] = entry
    return result


def prestej_tvite(tweets):
    temp = {}
    result = {}
    for tweet in tweets:
        entry = besedilo(tweet)
        key = tweet.split(":")[0]
        if key not in temp:
            temp[key] = [entry]
        else:
            temp[key].append(entry)
    for key in temp:
        lenght = len(temp[key])
        result[key] = lenght
    return result


def omembe(tweets):
    temp_words = []
    result = {}
    for tweet in tweets:
        key = tweet.split(":")[0]
        words = besedilo(tweet).split()
        if key not in result:
            result[key] = temp_words
        for word in words:
            if word.startswith("@"):
                word = izloci_besedo(word)
                if result[key] == []:
                    result[key] = [word]
                else:
                    result[key].append(word)
    return result


def neomembe(ime, omembe):
    mentions = []
    for key in omembe:
        if key not in omembe[ime] and key != ime:
            mentions.append(key)
    return mentions


### END obvezni del #####

###### dodatni del ######


def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.get(ime2, "0") or ime2 in omembe.get(ime1, "0"):
        return True
    else:
        return False


def hashtagi(tweets):
    result = {}
    authors = []
    for tweet in tweets:
        tweet_words = besedilo(tweet).split()
        for word in tweet_words:
            if word.startswith("#"):
                for tweet in tweets:
                    if word in tweet:
                        authors.append(tweet.split(":")[0])
                key = izloci_besedo(word)
                authors.sort()
                result[key] = authors
                authors = []
    return result


### END dodatni del #####

####### END naloga #######




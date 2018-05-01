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



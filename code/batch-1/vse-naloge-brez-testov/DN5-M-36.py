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




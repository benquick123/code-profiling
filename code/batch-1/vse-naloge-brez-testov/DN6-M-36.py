def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    tvit_dic = {}
    for tvit in tviti:
        tvit_dic[tvit.split(": ")[0]] = besedilo(tvit)
    return tvit_dic

def prvi_tvit(tviti):
    tvit_dic = {}
    for tvit in tviti:
        oseba = tvit.split(": ")[0]
        if oseba not in tvit_dic:
            tvit_dic[oseba] = besedilo(tvit)
    return tvit_dic

def prestej_tvite(tviti):
    tvit_dic = defaultdict(int)
    for tvit in tviti:
        oseba = tvit.split(": ")[0]
        tvit_dic[oseba] += 1
    return tvit_dic

def omemba(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def omembe(tviti):
    tvit_dic = defaultdict(list)
    for tvit in tviti:
        oseba = tvit.split(": ")[0]
        temp = tvit_dic[oseba]
        besede = tvit.split(" ")
        for beseda in besede:
            if beseda[0] == "@":
                om = omemba(beseda[1:])
                temp.append(om)
        tvit_dic[oseba] = temp
    return tvit_dic

def neomembe(ime, omembe):
    seznam_1 = omembe[ime]
    seznam_2 = []
    for omemba in omembe:
        if omemba not in seznam_1 and omemba != ime:
            seznam_2.append(omemba)
    return seznam_2

def se_poznata(ime1, ime2, omembe):
    for omemba in omembe:
        if omemba == ime1:
            seznam_1 = omembe[ime1]
            for element in seznam_1:
                if element == ime2:
                    return True
        if omemba == ime2:
            seznam_2 = omembe[ime2]
            for element in seznam_2:
                if element == ime1:
                    return True
    else: return False

def hashtagi(tviti):
    hashes = {}
    for tvit in tviti:
        oseba = tvit.split(": ")[0]
        besede = tvit.split()
        for beseda in besede:
            if beseda[0] == "#":
                hashtag = beseda[1:]
                while not hashtag[0].isalnum():
                    hashtag = hashtag[1:]
                while not hashtag[-1].isalnum():
                    hashtag = hashtag[:-1]
                if hashtag not in hashes:
                    hashes[hashtag] = [oseba]
                else:

                    hashes[hashtag].append(oseba)
                    hashes[hashtag] = sorted(hashes[hashtag])


    return hashes

def besedilo(tvit):
    return " ".join(tvit.split()[1:])


def zadnji_tvit(tviti):
    slovarij = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        slovarij[avtor] = besedilo(tvit)
    return slovarij


def prvi_tvit(tviti):
    return zadnji_tvit(tviti[::-1])


def prestej_tvite(tviti):
    slovarij = {}
    for tvit in tviti:
        avtor = tvit.split(":")[0]
        if avtor not in slovarij:
            slovarij[avtor] = 0
        slovarij[avtor] += 1
    return slovarij


def omembe(tviti):
    slovarij = {}
    for avtor_tvit in tviti:
        lista = []
        avtor = avtor_tvit.split()[0]
        tvit = avtor_tvit.split()[1:]
        for afna in tvit:
            if "@" in afna:
                while not afna[-1].isalnum():
                    afna = afna[:-1]
                lista.append(afna[1:])
        if avtor[:-1] in slovarij:
            for x in lista:
                slovarij[avtor[:-1]].append(x)
        elif avtor not in slovarij:
            slovarij[avtor[:-1]] = lista
    return slovarij


def neomembe(ime, omembe):
    lista = list(omembe.keys())
    lista_omembe = omembe[ime]
    lista_neomembe = []
    for x in lista:
        if x not in lista_omembe and x != ime:
            lista_neomembe.append(x)
    return lista_neomembe


def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe.keys() or ime2 not in omembe.keys():
        return False
    elif ime1 in omembe[ime2] or ime2 in omembe[ime1]:
        return True
    else:
        return False


def hashtagi(tviti):
    slovarij = {}
    for tvit in tviti:
        for h in tvit.split():
            if "#" in h:
                while not h[-1].isalnum():
                    h = h[:-1]
                slovarij[h[1:]] = []
    for hashtag in slovarij:
        lista_values = []
        for tvit in tviti:
            if hashtag in tvit:
                lista_values.append(tvit.split()[0][:-1])
        slovarij[hashtag] = sorted(lista_values)
    return slovarij



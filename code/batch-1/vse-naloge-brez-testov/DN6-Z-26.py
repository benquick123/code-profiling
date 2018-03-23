random_tviti = ["sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki - 1",
                "ema2: @benjamin @ana #split? po dvopičju, za začetek2?1",
                "ana: kdo so te @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "ema: @benjamin @ana #split? po dvopičju, za začetek?",
                "sandra: @berta Ne maram #programiranje1 #krneki - 2",
                "ema2: @benjamin @ana #split? po dvopičju, za začetek2?",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek2?223"]



#1
def besedilo(tvit):
    rezultat = ""
    if ":" in tvit:
        if tvit.split(':', 1)[1] != '':
            rezultat = tvit.split(':', 1)[1].lstrip()
    return rezultat


#2
def zadnji_tvit(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '':
            tvit_slovar[pretty_name] = posamezni_tvit[i].split(":")[1]
        i = i + 1
    return tvit_slovar


#3
def prvi_tvit(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '' and pretty_name not in avtorji: #v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = posamezni_tvit[i].split(":")[1]
            avtorji.append(pretty_name)
        i = i + 1
    return tvit_slovar


#4
def prestej_tvite(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '' and pretty_name not in avtorji: #v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = 1
            avtorji.append(pretty_name)
        else:
            tvit_slovar[pretty_name] += 1
        i = i + 1
    return tvit_slovar

#5
def vse_afne_v_enem_tvitu(tvit):
    besede = []
    beseda = ""
    zapisuj = False
    for chrka in tvit:
        if chrka == "@":
            zapisuj = True
        elif not chrka.isalnum() and beseda:
            if not beseda in besede:
                besede.append(beseda)
            beseda = ""
            zapisuj = False
        elif zapisuj:
            beseda += chrka
    if beseda and not beseda in besede:
        besede.append(beseda)
    return besede


def omembe(tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '':  # v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = vse_afne_v_enem_tvitu(posamezni_tvit[i])
            avtorji.append(pretty_name)
        i = i + 1
    return tvit_slovar

#6
def neomembe(ime, omembe):
    rezultat = []
    ime = ime.lower()
    omembe_ime = ""
    if ime in omembe: # Ana mora biti v seznamu
        omembe_ime = omembe[ime]
    else: return rezultat

    vsi_avtorji_v_omembe = [] #avtorji_tvitov
    for avtor in omembe:
        vsi_avtorji_v_omembe.append(avtor)
    vsi_avtorji_v_omembe.remove(ime)

    for avtor, avtorji_omenjeni in omembe.items():
        if avtor != ime and omembe_ime != '':  # avtor ni ana - izključimo 
            rezultat = vsi_avtorji_v_omembe
            for avtor_omenjeni in omembe_ime:
                if avtor_omenjeni in rezultat:
                    rezultat.remove(avtor_omenjeni)
    return rezultat



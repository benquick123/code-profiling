import re

def besedilo(tvit):
    rezi = tvit.split()
    text = tvit.lstrip(rezi[0])
    novi = text.lstrip(" ")
    return novi



def zadnji_tvit(tviti):
    slov = {}
    for tvit in tviti:
        uredi = tvit.split(":")
        txt = besedilo(tvit)
        avtor = uredi[0]
        slov[avtor] = txt
    return slov

def prvi_tvit(tviti):
    slov = {}
    for tvit in tviti:
        uredi = tvit.split(":")
        txt = besedilo(tvit)
        avtor = uredi[0]
        if avtor not in slov:
            slov[avtor] = txt
    return slov


def prestej_tvite(tviti):
    slov = {}
    for tvit in tviti:
        uredi = tvit.split(":")
        avtor = uredi[0]
        if avtor in slov:
            slov[avtor] += 1
        else:
            slov[avtor] = 1
    return slov

def omembe(tviti):
    slov = {}

    for tvit in tviti:
        sez = tvit.split()
        avtor = sez[0].strip(":")
        if avtor not in slov:
            slov[avtor] = []
        for beseda in sez:
            if beseda[0] == "@":
                shraniB = re.sub('[!;:,?)/%#@]', '', beseda)
                #shraniB = beseda.strip("@")
                if shraniB not in slov[avtor]:
                    slov[avtor].append(shraniB)
    return slov

def neomembe(ime, omembe):
    novslo = {}
    for oseba in omembe:
        if oseba not in novslo:
            novslo[oseba] = []
        for osebki in omembe.values():
            for vsak in osebki:
                if vsak not in omembe[oseba] and vsak != oseba and vsak in omembe.keys():
                    novslo[oseba].append(vsak)
    vrni = novslo[ime]
    return vrni

def se_poznata(ime1, ime2, omembe):
    for oseba,poznanci in omembe.items():
        if ime1 == oseba:
            if ime2 in poznanci:
                return True
        if ime2 == oseba:
            if ime1 in poznanci:
                return True
    return False

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        razdeli = tvit.split()
        avtor = razdeli[0].strip(":")

        for beseda in razdeli:
            if beseda[0] == "#":
                txt = beseda.strip("#").strip("?")
                if txt in slovar:
                    slovar[txt].append(avtor)
                    uredi = sorted(slovar[txt])
                    slovar[txt] = uredi
                if txt not in slovar:
                    slovar[txt] = [avtor]
    return slovar



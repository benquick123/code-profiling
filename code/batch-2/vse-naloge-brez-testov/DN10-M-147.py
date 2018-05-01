otroci = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}

def premozenje(oseba, denar):

    denarcic=denar[oseba]
    vsota=0
    for otrok in otroci[oseba]:
        vsota+=premozenje(otrok, denar)
    return vsota+denarcic

def najbogatejsi(oseba, denar):
    xs = [(oseba, denar[oseba])]

    for otrok in otroci[oseba]:
        xs.append(najbogatejsi(otrok, denar))

    #xs = ( oseba, denar )
    najpremoznejsi=-1

    for terka in xs:
        if isinstance(terka, list):
            for el in terka:
                if el[1] > najpremoznejsi:
                    najpremoznejsi = el[1]
        else:
            if terka[1] > najpremoznejsi:
                najpremoznejsi = terka[1]

    seznam=[]

    for terka in xs:
        if terka[1]==najpremoznejsi:
            seznam.append(terka)
    if len(seznam) == 1:
        return seznam[0]
    return seznam


def uravnotezeni(oseba, denar):
    return  True

def neuravnotezeni(oseba, denar):
    return None


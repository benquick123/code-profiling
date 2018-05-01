from operator import itemgetter

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





def premozenje(oseba,denar):


    dnar = denar[oseba]

    for otrok in otroci[oseba]:

        dnar= dnar + premozenje(otrok,denar)


    return dnar



def najbogatejsi(oseba,denar):

    seznam = [(oseba,denar[oseba])]

    for otrok in otroci[oseba]:
        seznam.append(najbogatejsi(otrok,denar))

    return max(seznam,key=itemgetter(1))




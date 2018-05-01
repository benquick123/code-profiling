#coding=utf-8
#from __future__ import unicode_literals



def premozenje(oseba, denar):

    if oseba == [] :
        return

    vsdenar = denar[oseba]
    for otrok in otroci[oseba] :
        vsdenar += premozenje(otrok, denar)
    return vsdenar


def najbogatejsi(oseba, denar):

    if oseba == [] :
        return

    najoseba = oseba
    najdenar = denar[oseba]
    for otrok in otroci[oseba] :
        novoseba, novdenar = najbogatejsi(otrok, denar)
        if novdenar > najdenar :
            najoseba = novoseba
            najdenar = novdenar

    return najoseba, najdenar


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



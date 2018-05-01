# -*- coding: utf-8 -*-
from random import *
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
    vsota = 0
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    vsota += denar[oseba]
    return vsota

def najbogatejsi(oseba, denar):
    naj = oseba
    for otrok in otroci[oseba]:
        if denar[otrok] > denar[naj]:
            naj = najbogatejsi(otrok,denar)[0]
    return (naj, denar[naj])

def uravnotezeni(oseba, denar):
    odg = True
    x = 0
    prm = 0
    for otrok in otroci[oseba]:
        if x == 0:
            prm = premozenje(otrok, denar)
            x += 1
        if (premozenje(otrok, denar) != prm) or (uravnotezeni(otrok, denar) == False):
            odg = False
    return odg

def neuravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        if (uravnotezeni(otrok, denar) == False):
            return neuravnotezeni(otrok, denar)

    if (uravnotezeni(oseba, denar) == False):
        return oseba


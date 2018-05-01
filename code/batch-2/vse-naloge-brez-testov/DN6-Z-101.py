def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    presledki = tvit.split()
    prvi = presledki[0]
    ime, text = prvi.split(":")
    return ime

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba1 == pisec and oseba2 in omenjeni or \
                oseba2 == pisec and oseba1 in omenjeni:
            return True
    return False

#Funkcija besedilo(tvit) prejme tvit
# in vrne besedilo - torej vse, kar sledi prvemu dvopičju.
# Klic besedilo("ana: kdo so te: @berta, @cilka, @dani?")
# vrne "kdo so te: @berta, @cilka, @dani?.

def besedilo(tvit):
    text = tvit[len(avtor(tvit))+2:]
    return text


#ce sta dva kluca ista se povozi vrednost

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        ime = avtor(tvit)
        tekst = besedilo(tvit)
        slovar[ime] = tekst
    return slovar

def prvi_tvit(tviti):
   z = {}
   for tvit in tviti[::-1]:
       ime = avtor(tvit)
       tekst = besedilo(tvit)
       z[ime] = tekst
       print(z)
   return z

def prestej_tvite(tviti):
    pogostosti = {}
    for tvit in tviti:
        ime = avtor(tvit)
        tekst = besedilo(tvit)
        if ime not in pogostosti:
            pogostosti[ime] = 0
        pogostosti[ime] += 1
    return pogostosti

from collections import defaultdict
from math import*

import itertools

def omembe(tviti):
   my_dict = {}
   for tvit in tviti:
       ime = avtor(tvit)
       omenjeni = se_zacne_z(besedilo(tvit), "@")
       if ime not in my_dict:
           my_dict[ime] = omenjeni
       else:
           my_dict[ime] += omenjeni
   print(my_dict)
   return my_dict

#Funkcija neomembe(ime, omembe) prejme ime neke osebe in takšen slovar, kakršnega vrne gornja funkcija.
# Vrniti mora seznam vseh ljudi, ki so avtorji kakega tvita, podana oseba (ime) pa jih ni omenjala.
# Če funkciji kot argument podamo ime "Ana" in gornji slovar, mora vrniti ["sandra", "benjamin],
# saj Ana ni omenjala Sandre in Benjamina, Cilko in Berto pa je. Iz seznama naj bo seveda
# izključena oseba sama (v tem primeru Ana). Vrstni red oseb v seznamu je lahko poljuben.

def neomembe(ime, omembe):
    seznam = list(omembe.keys())
    if ime in seznam:
        seznam.remove(ime)
    omembe_imena = omembe[ime]
    for omemba in omembe_imena:
        if omemba in seznam:
            seznam.remove(omemba)
    return seznam


















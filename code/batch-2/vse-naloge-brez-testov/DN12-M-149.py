import collections
import math
def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    krozisca = collections.defaultdict(list)    #ustvarimo prazen slovar
    for inx, vrstica in enumerate(datoteka):    #sprehod skozi datoteko
        vrstica = vrstica.replace('\n','').split(" ") #razdeli na vrstice ter znotraj vrstice odstrani presledke
        vrstica = [int(x) for x in vrstica] #spremenimo "str" v "int"
        for a in range(vrstica.index(min(vrstica)),vrstica.index(min(vrstica))+len(vrstica)):
            krozisca[inx+1].append(vrstica[a%len(vrstica)])
    datoteka.close()
    return krozisca

def mozna_pot(pot, zemljevid):
    for inx, krozisce in enumerate(pot):
        if len(zemljevid[pot[0]]) != 1:
            return False   #preverimo ali je začetno krožišče povezano s samo eno povezavo
        if inx + 1 == len(pot) and len(zemljevid[pot[inx]]) != 1:
            return False
        if len(zemljevid[pot[inx]]) == 1 and inx != 0 and inx + 1 < len(pot):
            return False
        if inx != 0:
            if pot[inx] not in zemljevid[pot[inx - 1]]:
                return False #preverimo ali so povezane
    return True

def hamiltonova(pot, zemljevid):

    if mozna_pot(pot, zemljevid):   #preveri ali je pot sploh možna
        stevilo = 0 #stevilo koncnih povezav
        for vrstica in zemljevid:
            if len(zemljevid[vrstica]) == 1:
                stevilo = stevilo + 1   #prišteva končne povezave
        if len(zemljevid) - stevilo + 2 != len(pot):
            return False
        return True

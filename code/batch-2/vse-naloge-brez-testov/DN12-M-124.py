import re
from itertools import cycle
import collections




def preberi(ime_datoteke):
    blabla=[]
    vrne={}
    kok=1
    naj=[]
    seznam=[]
    neki=1000
    lol=open(ime_datoteke)
    for vrstica in lol:
        bla=vrstica.split()
        bla=list(map(int,bla))
        for ti in bla:
            if ti<neki:

               tista=ti
               neki=ti
            seznam.append(ti)
        for fin in seznam:
            a=seznam.index(tista)

            b=seznam.index(fin)
            if a<=b:
                blabla.append(fin)
        l = [x for x in seznam if x not in blabla]
        l[0:0]=blabla

        blabla=[]




        neki = 1000
        vrne[kok]=l
        kok=kok+1
        seznam = []
    lol.close()
    return vrne

def mozna_pot(pot, zemljevid):
    koncne=[]
    stevec=0
    stevilo=1
    st=0
    seznam=[]
    pravi=[]
    vsa={}
    st=0
    sel=0
    toliko=0
    for e in zemljevid:
        if len(zemljevid[e])==1:
            koncne.append(e)
    tisto=0

    kolk = len(pot)
    kolk=kolk-1
    for t in pot:
        if t in koncne:
            toliko=toliko+1


    if toliko!=2:
        return False
    if pot[0] and pot[kolk]not in koncne:

        return False
    for one in pot:
        if sel!=kolk:
            tisti = pot.index(one) + 1
            if st==one:
                return False
            if pot[tisti] not in zemljevid[one]:

                return False
            sel=sel+1
        st==one
    return True
def hamiltonova(pot, zemljevid):
    koncne=[]
    mozna=[]
    vsa=[]
    tiste=[]
    if  mozna_pot(pot,zemljevid)==False:

        return False

    for l in zemljevid:
        vsa.append(l)
    for e in zemljevid:
        if len(zemljevid[e])==1:
            koncne.append(e)
    for ko in pot:
        mozna.append(ko)
    for el in koncne:
        vsa.remove(el)


    for cc in mozna:
        if cc not in koncne:
            tiste.append(cc)


    if collections.Counter(vsa) == collections.Counter(tiste):
        return True
    else:
        return False









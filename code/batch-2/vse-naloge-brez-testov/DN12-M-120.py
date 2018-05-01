def preberi(ime_datoteke):

    slovar_krizisc = {}
    a = 1
    datoteka=open(ime_datoteke)

    def red(x):
        y=1000
        for a in range(len(x)):
            if x[a]<y:
                y=x[a]
                ind=a
        return x[ind:]+x[:ind]

    for x in datoteka:
        table=re.split(r' +',x)
        for y in range(len(table)):
            table[y]=int(table[y])
        table=red(table)
        slovar_krizisc[a]=table
        a = a+1

    return slovar_krizisc





def mozna_pot(pot, zemljevid):

    if len(zemljevid[pot[0]])!=1 or len(zemljevid[pot[-1]])!=1:
        return False

    for i in range(len(pot)-1):

        if pot[i+1] not in zemljevid[pot[i]]:
            return False

        if len(zemljevid[pot[i]])==1 and i!=0:
            return False

    return True





def hamiltonova(pot, zemljevid):

    seznam=[]

    if mozna_pot(pot,zemljevid) == False:
        return False

    for i in zemljevid:
        if len(zemljevid[i])==1 and i not in pot:
            seznam.append(i)

    pot.sort()
    tab = [i for i in range(1,max(pot)+1)]

    for x in seznam:
        tab.remove(x)

    if pot==tab:
        return True
    else:
        return False



from random import randint
import re


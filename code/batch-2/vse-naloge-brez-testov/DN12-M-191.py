__author__ = 'Haris'

def preberi(ime_datoteke):
    output={}
    datoteka=open(ime_datoteke)
    i=1
    for vrstica in datoteka:
        razclenjena_vrstica=vrstica.strip().split()
        int_vrstica=[int(e) for e in razclenjena_vrstica]
        j=0
        s=int_vrstica
        while j<len(int_vrstica):
            if int_vrstica[j] == min(int_vrstica) and len(int_vrstica)>1:
                s=int_vrstica[j:]+int_vrstica[:j]
            j+=1
        output[i]=s
        i+=1
    return output

def mozna_pot(pot, zemljevid):
    #mapa=preberi(zemljevid)
    mapa=zemljevid
    i=1
    s=set()
    for elementi in mapa:
        if len(mapa[elementi])==1:
            s.add(elementi)

    for elementi in pot:
        prvi=pot[0]
        zadnji=pot[-1]
        if len(pot)>2:
            for element in pot[1:-2]:
                if element in s:
                    return False


        if len(mapa[prvi])>1 or len(mapa[zadnji])>1 or len(pot)<2:
            return False
        else:
            while i<len(pot):
                if not mapa[pot[i]].__contains__(pot[i-1]):
                    return False

                i+=1

    return True

def hamiltonova(pot, zemljevid):
    vhodi=set()
    vozlisca=set()
    prevozena_pot=set()

    for elementi in zemljevid:
        if len(zemljevid[elementi])==1:
            vhodi.add(elementi)
        else:
            vozlisca.add(elementi)
    if mozna_pot(pot,zemljevid):
        for element in pot[1:-1]:
            if element not in prevozena_pot:
                prevozena_pot.add(element)
            else:
                return False
        if len(prevozena_pot)==len(vozlisca):
            return True
        else:
            return False
    else:
        return False



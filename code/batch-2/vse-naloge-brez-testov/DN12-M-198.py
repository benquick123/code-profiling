######OCENA 6
def pridobi(ime_datoteke):
    dic = {}
    n=1
    file=open(ime_datoteke)
    for vrstica in file:
        dic[n] = list()
        dic[n].extend([int(a) for a in vrstica.strip().split(' ')])
        n+=1
    file.close()
    return dic

def preberi(ime_datoteke):
    dic=pridobi(ime_datoteke)
    tdic=dic.copy()
    for key,value in dic.items():
        m=min(value)
        t=value
        i=0
        while i< len(value):
            if value[0]==m:
                tdic[key]=t
                break
            else:
                t.append(t.pop(0))
    return tdic
                
def povezan(k1,k2,zemljevid):
    for key,value in zemljevid.items():
        if key==k1:
            for a in value:
                if a==k2:
                    return True
    return False


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]])==1 and len(zemljevid[pot[len(pot)-1]])==1:
        i=1
        while i<len(pot):
            if povezan(pot[i-1], pot[i],zemljevid):
                if i<len(pot)-1:#če ni tazadn
                    if len(zemljevid[pot[i]])==1:#ne sme bit končni
                        return False
            else:
                return False
                        
            i+=1
            
        return True
    else:
        return False


def hamiltonova(pot, zemljevid):#skozi vsakega natančno enkrat
    if mozna_pot(pot,zemljevid):
        temp=[]
        for korak in pot:
            if korak in temp:#podvojeni
                return False
            temp.append(korak)
        
        for key,value in zemljevid.items():
            if key not in temp[:-1]:#če kateri manjka
                if len(value)>1:
                    return False
    else:
        return False
    return True



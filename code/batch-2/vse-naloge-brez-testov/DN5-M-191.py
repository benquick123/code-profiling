__author__ = 'Haris'

def unikati(s):
    rezultat=[]
    for element in s:
        if element not in rezultat:
            rezultat.append(element)
    return rezultat

def avtor(tvit):
    razsekan_tvit=tvit.split(":")
    return razsekan_tvit[0]

def vsi_avtorji(tviti):
    seznam1=[]
    for niz in tviti:
        seznam1.append(avtor(niz))
    return unikati(seznam1)

def izloci_besedo(beseda):
    output=beseda
    i=0
    while not beseda[i].isalnum():
        i+=1
    output=beseda[i:]
    f=-1
    while not output[f].isalnum():
        f-=1
        output=output[:f+1]
    return output

def se_zacne_z(tvit, c):
    seznam=tvit.split()
    output=[]
    for element in seznam:
        if element.startswith(c):
            output.append(izloci_besedo(element))
    return output

def zberi_se_zacne_z(tviti, c):
    output=[]
    for stavek in tviti:
        puding=se_zacne_z(stavek, c)
        for element in puding:
            if element not in output:
                output.append(element)
    return output
#za lazjo izvedbo zadnje obvezne
def se_konca_z(tvit,c):
    seznam=tvit.split()
    output=[]
    for element in seznam:
        if element[-1]==c:
            output.append(izloci_besedo(element))
    return output

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    output=zberi_se_zacne_z(tviti, "@")
    for stavek in tviti:
        puding=se_konca_z(stavek,":")
    for element in puding:
        output.append(element)
    return sorted(output)

def custva(tviti, hashtagi):
    output=[]
    for stavek in tviti:
        for tag in hashtagi:
            if "#"+tag in stavek.split() and avtor(stavek) not in output:
                output.append(avtor(stavek))

    return sorted(output)

def se_poznata(tviti, oseba1, oseba2):
    for stavek in tviti:
        stavek=stavek.replace(",","")
        if avtor(stavek)==oseba1:
            if "@"+oseba2 in stavek.split():
                return True
                break
        if avtor(stavek)==oseba2:
            if "@"+oseba1 in stavek.split():
                return True
                break
    return False

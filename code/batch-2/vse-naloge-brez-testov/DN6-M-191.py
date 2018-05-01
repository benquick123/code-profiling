__author__ = 'Haris'

def besedilo(tvit):
    output=""
    i=0
    for znak in tvit:
        i+=1
        if znak==":":
            output=tvit[i+1:]
            break
    return output

def avtor(tvit):
    output=""
    i=0
    for znak in tvit:
        i+=1
        if znak==":":
            output=tvit[:i-1]
            break
    return output


def zadnji_tvit(tviti):
    output={}
    for tvit in tviti:
        output[avtor(tvit)]=besedilo(tvit)
    return output

def prvi_tvit(tviti):
    output={}
    for tvit in tviti:
        if avtor(tvit) not in output:
            output[avtor(tvit)]=besedilo(tvit)
    return output

def prestej_tvite(tviti):
    output={}
    for tvit in tviti:
        if avtor(tvit) not in output:
            output[avtor(tvit)]=1
        elif avtor(tvit) in output:
            output[avtor(tvit)]+=1
    return output

"""kopija kode iz dn05"""


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

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")
def omembe(tviti):
    output={}
    for tvit in tviti:
        if avtor(tvit) not in output:                   #obstaja možnost da neka beseda tvitne dvakrat in bo drugi tvit povozil prvega
            output[avtor(tvit)]=vse_afne([tvit])
        else:
            for oseba in vse_afne([tvit]):
                if oseba not in output[avtor(tvit)]:
                    output[avtor(tvit)].append(oseba)
    return output

def neomembe(ime, omembe):
    seznam=[]
    for osebe in omembe:
        if osebe not in omembe[ime] and osebe != ime:
            seznam.append(osebe)
    return seznam

def se_poznata(ime1, ime2, omembe):
    if ime1 not in neomembe(ime2,omembe) and ime2 not in neomembe(ime1,omembe):
        return True
    else:
        return False




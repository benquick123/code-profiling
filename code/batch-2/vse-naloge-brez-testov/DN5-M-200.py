def unikati(s):
    unikat = []
    for i in s:
        if i in unikat:
            continue
        else:
            unikat.append(i)
    return unikat

def avtor(tvit):
    return tvit.split (":")[0]
    
def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)
    

def izloci_besedo(beseda):
    nova_beseda = list(beseda)
    return "".join([i for i in nova_beseda if i.isalnum () or i == '-'])
            
        
def se_zacne_z (tvit, c):
    seznam = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            seznam.append(izloci_besedo(beseda))
    return seznam
    
def zberi_se_zacne_z(tviti, c):
    zbrano = []
    brez = []
    for tvit in tviti:
        zbrano.extend(se_zacne_z(tvit, c))
    for i in zbrano: 
        if i not in brez: 
            brez.append(i)
    return brez


def vse_afne (tviti):
    return zberi_se_zacne_z(tviti, "@")
    
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti)
    afne = vse_afne (tviti)
    return sorted(unikati(avtorji + afne))

def custva(tviti, hashtagi):
    seznam_oseb = []
    for hashtag in hashtagi:
        for tvit in tviti:
           if hashtag in tvit:
               seznam_oseb.append(avtor(tvit))
    return sorted(unikati(seznam_oseb))
               
def se_poznata(tviti, oseba1, oseba2):
    stanje = False
    for tvit in tviti:
        if (oseba1 in tvit) and ('@' + oseba2 in tvit):
            stanje = True
            return stanje
        else:
            continue
    return stanje





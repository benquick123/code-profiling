def besedilo(tvit):
    pozicija = tvit.index(":")
    return tvit[pozicija+2::]

def pomozna(tvit1):
    pozicija =tvit1.index(":")
    return tvit1[:pozicija]
    

def zadnji_tvit(tviti):
    slovar = {}
    for t in tviti:
        ime = pomozna(t)
        slovar[ime] = besedilo(t)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for t in tviti:
        ime = pomozna(t)
        if ime in slovar.keys():
            pass
        else:
            slovar[ime] = besedilo(t)
    return slovar

def prestej_tvite(tviti):
    slovar ={}
    for t in tviti:
        ime = pomozna(t)
        if ime in slovar.keys():
            slovar[ime] += 1
        else:
            slovar[ime] = 1
        
    return slovar

def imena(tviti):
    seznam = []
    crke = 'abcdefghijklmnopqrstuvwxyz'
    noviEl = ''
    for t in tviti:
        bes = besedilo(t)
        for el in bes.split(" "):
            if '@' in el:
                seznam.append(el)
                
    return seznam


def neomembe(ime, omembe):
    sezImen = []
    osebe = omembe[ime]
    koncno = []
    for imena in omembe.keys():
        if imena not in sezImen:
                sezImen.append(imena)
    for i in sezImen:
        if i not in osebe:
            koncno.append(i)
    koncno.remove(ime)
    return koncno
            
            
        
def omembe(tviti):
    imenaSez = imena(tviti)
    slovar = {}
    novi = []
    noviEl = ''
    crke = 'abcdefghijklmnopqrstuvwxyz'
    for t in tviti:
        bes = besedilo(t)
        ime = pomozna(t)
        for el in bes.split(" "):
            if el in imenaSez:
                for c in el:
                    if c in crke:
                        noviEl += c
                novi.append(noviEl)
            noviEl = ''
        if ime in slovar.keys():
            slovar[ime] += novi
        else:
            slovar[ime] = novi
        novi = []
    return slovar













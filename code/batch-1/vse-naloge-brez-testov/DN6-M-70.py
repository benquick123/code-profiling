def besedilo(tvit):
    c=0
    for crka in tvit:
        c+=1
        if crka == ":":
            return tvit[c+1:]
        
def avtor(tvit):
    return tvit.split(":")[0]

def zadnji_tvit(tviti):
    tvitis={}
    for tvit in tviti:
        tvitis[avtor(tvit)]=besedilo(tvit)
    return tvitis

def prvi_tvit(tviti):
    tvitis={}
    for tvit in tviti:
        if avtor(tvit) not in tvitis:
            tvitis[avtor(tvit)]=besedilo(tvit)
    return tvitis
def prestej_tvite(tviti):
    tvitis={}
    for tvit in tviti:
        if avtor(tvit) not in tvitis:
            tvitis[avtor(tvit)]=1
        else:
            tvitis[avtor(tvit)]+=1
    return tvitis

def omembe(tviti):
    tvitis={}
    for tvit in tviti:
        tvitis[avtor(tvit)]=[]
    for tvit in tviti:
        for beseda in tvit.split():
            if beseda.startswith("@"):
                tvitis[avtor(tvit)].append((izloci_besedo(beseda)))
    return tvitis
def neomembe(ime, omembe):
    seznam =[]
    t=[]
    for avtor,x in omembe.items():
        if avtor == ime:
            t=x
    for avtor, omenjeni in omembe.items():
        if not avtor == ime:
            if avtor not in t:
                seznam.append(avtor)
        
    return seznam
                    




#DODATNE
def se_poznata(ime1, ime2, omembe):
    for avtor,seznam in omembe.items():
        for oseba in seznam:
            if oseba == ime1:
                if avtor ==ime2:
                    return True
            elif oseba == ime2:
                if avtor == ime1:
                    return True
    return False

def hashtagi(tviti):##ni nastavljeno sortirnaje
    slovar = {}
    for tvit in tviti:
        for beseda in tvit.split():
            if izloci_besedo(beseda) in vsi_hashtagi(tviti):
                if izloci_besedo(beseda) not in slovar:
                    slovar[izloci_besedo(beseda)]=[]
                    slovar[izloci_besedo(beseda)].append(avtor(tvit))
                else:
                    slovar[izloci_besedo(beseda)].append(avtor(tvit))
    for hashtag, avtorji in slovar.items():
        avtorji.sort()
    
    return slovar
#pomožne
def unikati(s):
    t=[]
    for vsak in s:
        if vsak not in t:
            t.append(vsak)
    return t
    
def izloci_besedo(beseda):
    ok=False
    while not ok:
        if not beseda[0].isalnum():
            beseda=beseda[1:]
        elif not beseda[len(beseda)-1].isalnum():
            beseda=beseda[:-1]
        else:
            ok=True
    return beseda

def se_zacne_z(tvit,c):
    besede=[]
    for beseda in tvit.split():
        if beseda.startswith(c):
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    besede=[]
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit,c))
    return unikati(besede)

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")




#OBVEZNI DEL

#Unikati
def unikati(s):
    s_unikati = []
    for i in s:
        if i not in s_unikati: #preveri, če se element še ni pojavil
            s_unikati.append(i) #doda nov element
    return s_unikati

#Avtor
def avtor(tvit):
    s = tvit.split() #spremeni 'tvit' v seznam
    avtor = s[0] #vzame prvo besedo (avtorja)
    return avtor[:-1] #vrne brez ':'

#Vsi avtorji
def vsi_avtorji(tviti):
    avtorji = []
    for i in tviti: #iz vseh tvitov
        avtorji.append(avtor(i)) #zabeleži avtorje
    return unikati(avtorji) #in vrne vse unikatne

#Izloči besedo (brez 'čudnih' znakov)
def izloci_besedo(beseda):
    samo_beseda = ""
    for char in beseda:
        if char.isalnum() or char == '-': #preveri, če je simbol črka ali '-'
            samo_beseda += char #doda novi besedi
    return samo_beseda

#Se začne z ...
def se_zacne_z(tvit, c):
    besede = tvit.split() #razdeli besede v seznam
    iskane_besede = []
    for i in besede:
        if i.startswith(c): #če se beseda začne z iskanim znakom
            iskane_besede.append(izloci_besedo(i)) #doda besedo brez 'čudnih' znakov
    return iskane_besede

#Zberi 'Se začne z ...' (iz vseh tvitov)
def zberi_se_zacne_z(tviti, c):
    besede = []
    iskane_besede = []
    for tvit in tviti: #vsak tvit posebej
        besede.append(se_zacne_z(tvit,c)) #zbere vse besede (v podsezname za posamezen tvit)
    for i in besede:
        for j in i:
            if j not in iskane_besede: #ker so besede prej v podseznamih
                iskane_besede.append(j) #unikate prepišemo v nov seznam
    return iskane_besede #lahko tudi z return unikati(iskane_besede), namesto zadnjega if-stavka

#Vse afne
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@') #zbere vse besede iz vseh tvitov, ki se začnejo z '@'

#Vsi hashtagi
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#') #zbere vse besede iz vseh tvitov, ki se začnejo z '#'

#Vse osebe
def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti) #poiščemo vse avtorje
    omenjeni = vse_afne(tviti) #poiščemo vse omenjene osebe
    osebe = []
    for i in avtorji:
        if i not in osebe:
            osebe.append(i) #vse poiskane dodamo v seznam, brez ponavljanj
    for i in omenjeni:
        if i not in osebe:
            osebe.append(i)
    return sorted(osebe) #seznam uredimo po abecedi


#DODATNI DEL

#Čustva (osebe, ki so uporabile določen '#')
def custva(tviti, hashtagi):
    osebe = []
    for tvit in tviti:
        for i in se_zacne_z(tvit, '#'): #poišče vse besede, ki se začnejo z '#'
            if i in hashtagi: #če so to iskane besede
                osebe.append(avtor(tvit)) #si zapomni avtorja
    return sorted(unikati(osebe)) #seznam uredi in izloči duplikate

#Se poznata
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1 == avtor(tvit) or oseba2 == avtor(tvit): #če je ena od oseb avtor
            if oseba2 in se_zacne_z(tvit, '@') or oseba1 in se_zacne_z(tvit, '@'): #in omeni drugo osebo
                return True #potem se poznata
    return False


#TESTI (ne spreminjaj)


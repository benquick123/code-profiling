'''
        Program: različne naloge s slovarji in seznami
        Avtor: Blaž Kumer
        Datum: 16. 11. 2017


'''




from collections import defaultdict
#izloči vse nealfanumerične znake na začetku in koncu besede
def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

#vrne besedilo tvita brez avtorja
def besedilo(tvit):
    for i in range(len(tvit)):
        if not tvit[i].isalnum():
            break
    return tvit[i+2:]

#vrne slovar ki vsebuje zadnje tvite posameznih avtorjev
def zadnji_tvit(tviti):
    d={}
    for t in tviti:
        x=t.split(":")
        d.update({x[0]: besedilo(t)})
    return d

#vrne slovar s prvim tvitom posameznega avtorja
def prvi_tvit(tviti):
    d={}
    for t in tviti:
        x=t.split(":")
        if x[0] not in d.keys():
            d.update({x[0]: besedilo(t)})
    return d

#vrne slovar v katerem je napisano število tvitov avtorja
def prestej_tvite(tviti):
    d= defaultdict(int)
    for t in tviti:
        s=t.split(":")
        d[s[0]]+=1
    return d


#vrne slovar oseb ki so jih avtorji omenili v svojih tvitih
def omembe(tviti):
    d=defaultdict(list)
    for t in tviti:
        s=t.split(":")
        x=t.split(" ")
        if s[0] not in d.keys():
            d[s[0]]=[]
        for i in x:
            if i[0]=="@":
                d[s[0]].append(izloci_besedo(i))
    return d

# vrne slovar oseb ki jih avtorji niso omenili v svojih tvitih, a so avtorji tvitov
def neomembe(ime, omembe):
    sez = omembe.keys()
    konSez=[]
    x= omembe[ime]
    for s in sez:
        if s not in x and s!=ime :
            konSez.append(s)
    return konSez


#vrne true, če ena od oseb omeni drugo v svojem tvitu
def se_poznata(im1, im2, omembe):
    for im in omembe:
        if im==im1:
            break
    else:
        return False
    if im2 in omembe[im]:
        return True
    for i in omembe:
        if i == im2:
            break
    else:
        return False
    if im1 in omembe[i]:
        return True
    return False


#vrne slovar oseb ki so uporabili določen hešteg
def hashtagi(tviti):
    d= defaultdict(list)
    for tvit in tviti:
        besede= tvit.split(" ")
        for beseda in besede:
            if beseda[0]=="#":
                if izloci_besedo(beseda) not in d:
                    d.update({izloci_besedo(beseda) : [izloci_besedo(besede[0])]})
                else:
                    d[izloci_besedo(beseda)].append(izloci_besedo(besede[0]))
    for k in d:
        d[k]=sorted(d[k])
    return d



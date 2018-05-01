import re
def besedilo(tvit):
    b = []
    b.append(tvit)
    for x in b:
        a=x.split(": ", 1)
        return a[1]




def zadnji_tvit(tviti):
    seznam = {}
    for tvit in tviti:
        kljuc = tvit.split(":")[0]
        seznam[kljuc] = besedilo(tvit)
    return seznam

def prvi_tvit(tviti):
    seznam = {}
    for tvit in tviti:
        kljuc = tvit.split(":")[0]
        if kljuc not in seznam:
            seznam[kljuc] = besedilo(tvit)
        else:
            pass
    return seznam

def prestej_tvite(tviti):
    pogostosti = {}
    for tvit in tviti:
        kljuc = tvit.split(":")[0]
        if kljuc not in pogostosti:
            pogostosti[kljuc] = 0
    for tvit in tviti:
        kljuc = tvit.split(":")[0]
        pogostosti[kljuc] += 1
    return pogostosti

def omembe(tviti):
    pogostosti = {}
    v_tvitih = []
    for tvit in tviti:
       kljuc = tvit.split(":")[0]
       if kljuc == kljuc:
            v_tvitih.append(imena(tvit))
       if kljuc not in pogostosti:
           pogostosti[kljuc] = v_tvitih

def imena(tvit):
    imena_v_tvitih = []
    vrstica_besedila = tvit.split()
    for immena in vrstica_besedila:
        if immena.startswith("@"):
            imena_v_tvitih.append(samo_beseda(immena))


def samo_beseda(immena):
    a = re.compile("[A-Za-z]").findall(immena)
    b = sum(int(i) for i in a)
    return b

def neomembe(ime, omembe):
    omenil = []
    ni_omenil = []
    for tisti in omembe:
        omenil.append(tisti)
    for i in omenil:
        if i not in omembe[ime] and i != ime:
            ni_omenil.append(i)
        if i not in omembe[ime] and i == ime:
            pass
    return ni_omenil


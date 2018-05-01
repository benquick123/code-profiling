def besedilo(tvit):
    return tvit.split(":", 1)[1].strip()


def avtor(tvit):
    return tvit.split(":")[0]


def zadnji_tvit(tviti):
    tviti_dict = {}
    for tvit in tviti:
        tviti_dict[avtor(tvit)] = besedilo(tvit)
    return tviti_dict


def prvi_tvit(tviti):
    tviti_dict = {}
    for tvit in tviti:
        if not tviti_dict.get(avtor(tvit)):
            tviti_dict[avtor(tvit)]=besedilo(tvit)
    return tviti_dict


def prestej_tvite(tviti):
    presteti_tviti = {}
    for tvit in tviti:
        if not presteti_tviti.get(avtor(tvit)):
            presteti_tviti[avtor(tvit)] = 1
        else:
            presteti_tviti[avtor(tvit)] += 1
    return presteti_tviti

def izloci_besedo(beseda):
    seznam_crk = list(beseda)
    i = 0
    while i < len(seznam_crk):
        if not seznam_crk[i].isalnum():
            del seznam_crk[i]
            i=0
        else:
            break
    j = len(seznam_crk)-1
    while j >= 0:
        if not seznam_crk[j].isalnum():
            del seznam_crk[j]
        else: break
        j-=1
    return "".join(seznam_crk)

def se_zacne_z(tvit, c):
    besede = tvit.split()
    ujemajoce_besede = []
    for b in besede:
        if b[0] == c:
            ujemajoce_besede.append(izloci_besedo(b))
    return ujemajoce_besede


def omembe(tviti):
    omembe_dict = {}
    for tvit in tviti:
        omembe_v_tvitu = se_zacne_z(besedilo(tvit), "@")
        if not omembe_dict.get(avtor(tvit)):
            omembe_dict[avtor(tvit)] = []
        omembe_dict[avtor(tvit)].extend(omembe_v_tvitu)

    return omembe_dict


def neomembe(ime, omembe):
    omenjene_osebe = omembe[ime]
    vse_osebe = list(omembe.keys())
    neomemenjene_osebe = []
    for o in vse_osebe:
        if not o in omenjene_osebe and o != ime:
            neomemenjene_osebe.append(o)
    return neomemenjene_osebe



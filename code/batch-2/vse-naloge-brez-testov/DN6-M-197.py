from collections import defaultdict, Counter

def besedilo(tvit):
    breakpoint = tvit.index(":")
    tekst = tvit[breakpoint+2:]
    return tekst

def avtor(tvit):
    breakpoint = tvit.index(":")
    avtor = tvit[:breakpoint]
    return avtor

def zadnji_tvit(tviti):

    zadnji_tviti = defaultdict()
    for tvit in tviti:
        pisc = avtor(tvit)
        tekst = besedilo(tvit)
        zadnji_tviti[pisc] = tekst
    return (zadnji_tviti)

def prvi_tvit(tviti):
    prvi_tviti = defaultdict()
    for tvit in tviti:
        pisc = avtor(tvit)
        tekst = besedilo(tvit)
        if pisc not in prvi_tviti.keys():
            prvi_tviti[pisc] = tekst
    return (prvi_tviti)

def prestej_tvite(tviti):
    avtorji = [avtor(x) for x in tviti]
    return Counter(avtorji)
"""
infrastruktura za luščenje omenjenih oseb
"""
def unikati (s):
    uniqe_elements = []
    for unit in s:
        if unit not in uniqe_elements:
            uniqe_elements.append(unit)
    return uniqe_elements

def izloci_besedo(beseda):
    start = 0
    end = 0
    for char in beseda:
        if char.isalnum():
            start = beseda.index(char)
            break
    for char in beseda[::-1]:
        if char.isalnum():
            end = beseda.rindex(char)
            break
    return(beseda[start:end+1])

def vsi_start(besedilo, key):
    front = [izloci_besedo(x) for x in besedilo.split() if x[0] == key]
    return unikati(front)

def omembe(tviti):

    po_osebah = defaultdict(lambda : [])
    for tvit in tviti:
        po_osebah[avtor(tvit)] += (vsi_start(tvit, "@"))
    return po_osebah

def neomembe(ime, osebe):
    avtorji = osebe.keys()
    omenjeni = osebe[ime] + [ime]
    neomenjeni = [oseba for oseba in avtorji if oseba not in omenjeni]
    return neomenjeni

"""
do sem je za omembe
"""

def se_poznata(ime1, ime2, omembe):

    avtorji = omembe.keys()

    if ime1 in avtorji:
        if ime2 in omembe[ime1]:
            return True
    if ime2 in avtorji:
        if ime1 in omembe[ime2]:
            return True
    else:
        return False

def hashtagi(tviti):
    avtorji_po_hashih = defaultdict(lambda : [])
    for tvit in tviti:
        for tag in vsi_start(tvit, "#"):
               avtorji_po_hashih[tag] += [avtor(tvit)]

    output = defaultdict(lambda: [])
    for tag, avtorji in avtorji_po_hashih.items():
                   output[tag] += sorted(unikati(avtorji))
    return (output)



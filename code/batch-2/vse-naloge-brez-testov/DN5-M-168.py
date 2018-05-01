
def unikati(s):
    st = []
    for stevila in s:
        if stevila not in st:
            st.append(stevila)
    return st

def avtor(tvit):
    x1 = tvit.split()
    x = x1[0]
    b = x[:-1]
    return b

def vsi_avtorji(tviti):
    s = []
    for tvita in tviti:
      x = avtor(tvita)
      if x not in s:
        s.append(x)
    return s

def izloci_besedo(beseda):
    import re
    beseda1 = re.sub('[!@#$%"=%/%()/]', '', beseda)
    beseda1 = re.sub("[!@#$,%='%/?%()/]", '', beseda1)
    beseda2 = beseda1.lstrip()
    beseda3 = beseda2.rstrip()
    return beseda3

def se_zacne_z(tvit, c):
    s = []
    x = tvit.split()
    for y in x:
        if y.startswith(c):
            z = y
            g = izloci_besedo(z)
            s.append(g)
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        t = se_zacne_z(tvit, c)
        if t not in s:
            s = s + t
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(osebe)






















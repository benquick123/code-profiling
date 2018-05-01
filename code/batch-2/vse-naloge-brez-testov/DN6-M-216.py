def unikati(s):
    niza=[]
    for i in s:
        if i not in niza:
            niza.append(i)
    return niza

def avtor(tvit):
    tvit=tvit.split(" ")
    imena=tvit[0]
    imena=imena.replace(":",(""))
    return imena

def vsi_avtorji(tviti):
    avtor_beseda=[]
    for beseda in tviti:
        avtor_beseda.append(avtor(beseda))
    return unikati(avtor_beseda)

def izloci_besedo(beseda):
    dolz=len(beseda)
    i=0
    bukvi=[]
    zbor=""
    while i < dolz:
        if beseda[i] in ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",
                         "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",
                         "1","2","3","4","5","6","7","8","9","0"]:
           bukvi.append(beseda[i])
           zbor=zbor+str(beseda[i])
        elif beseda[i]=="-":
           bukvi.append("-")
           zbor = zbor+"-"
        i+=1
    return zbor




def se_zacne_z(tvit, c):
    besed_tvit = tvit.split()
    rezultat=[]
    for beseda in besed_tvit:
        if beseda[0] == c:
            rezultat.append(izloci_besedo(beseda))
    return rezultat

def zberi_se_zacne_z(tviti, c):
    besede_so_zacetak_c=[]
    rezultat=[]
    for beseda in tviti:
        besede_so_zacetak_c=se_zacne_z(beseda,c)
        for clen in besede_so_zacetak_c:
            if clen not in rezultat:
                rezultat.append(clen)
    return rezultat

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    afne=vse_afne(tviti)
    avtorji=vsi_avtorji(tviti)
    s = afne+avtorji
    s.sort()
    return unikati(s)

def custva(tviti, hashtagi):
    s=[]
    for tvit in tviti:
        for i in hashtagi:
            if i in tvit:
                s.append(avtor(tvit))
    s.sort()
    return unikati(s)





def besedilo(tvit):
    c=0
    while c<1000:
        if tvit[c] == ":":
            break
        c+=1
    return tvit[c+2:]

def zadnji_tvit(tviti):
    avtori = vsi_avtorji(tviti)
    dictionary = dict.fromkeys(avtori)
    for i in tviti:
        s = i.split(':')
        dictionary[s[0]] = besedilo(i)
    return dictionary

def prvi_tvit(tviti):
    avtori = vsi_avtorji(tviti)
    dictionary = dict.fromkeys(avtori,None)
    for i in tviti:
        s = i.split(':')
        if dictionary[s[0]]== None:
            dictionary[s[0]] = besedilo(i)
    return dictionary

def prestej_tvite(tviti):
    avtori = vsi_avtorji(tviti)
    dictionary = dict.fromkeys(avtori, 0)
    for i in tviti:
        s = i.split(':')
        dictionary[s[0]] += 1
    return dictionary

def omembe(tviti):
    avtori = vsi_avtorji(tviti)
    dictionary = dict.fromkeys(avtori, None)
    for i in tviti:
        s = i.split(':')
        if dictionary[s[0]] == None:
            dictionary[s[0]] = se_zacne_z(i, '@')
        else:
            dictionary[s[0]] += se_zacne_z(i, '@')
    return dictionary

def neomembe(ime, omembe):
    avtori = list(omembe.keys())
    avtori.remove(ime)
    for i in omembe[ime]:
        if i in avtori:
            avtori.remove(i)
    return avtori





def se_poznata(ime1, ime2, omembe):
    nisto=False
    if ime1  in omembe and ime2  in omembe:
        for omen in omembe:
            lalalla1=neomembe(ime1, omembe)
            lalalla2=neomembe(ime2, omembe)
            if ime1==omen:
                if ime2 not in neomembe(ime1, omembe) :
                    nisto = True
                    break
            elif ime2==omen:
                if ime1  not in neomembe(ime2, omembe):
                    nisto = True
                    break
                elif ime2 not in neomembe(ime1, omembe):
                    nisto = True
                    break
    return nisto



def hashtagi(tviti):
    dictionary = dict.fromkeys(vsi_hashtagi(tviti), None)
    for i in tviti:
        hashtags = se_zacne_z(i, '#')
        for j in hashtags:
            if dictionary[j] == None:
                dictionary[j] = [avtor(i)]
            else:
                dictionary[j] += [avtor(i)]
    for i in list(dictionary.keys()):
        dictionary[i].sort()
    return dictionary



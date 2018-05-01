
def avtor(tvit):
    t2 = []
    for črka in tvit:
        if črka != ":":
            t2.append(črka)

        else:
           return "".join (t2)

    return t2

def unikati (s):
    se= []
    for stvar in s:
        if stvar not in se:
            se.append (stvar)
    return se

def se_zacne_z(tvit, c):
    s=[]
    tviti=tvit.split()

    for beseda in tviti:
        if beseda.startswith(c):
            s.append( izloci_besedo(beseda))
    return s

def izloci_besedo(beseda):
    s=[]

    for letter in beseda:
        if letter.isalnum () or letter== "-":
            s.append(letter)

    def custva(tviti, hashtagi):
        s = []
        for tvit in tviti:
            avtor1 = avtor(tvit)
            hash = se_zacne_z(tvit, "#")
            for tag in hashtagi:
                if (tag in hash):
                    s.append(avtor1)

        s.sort()

        return unikati(s)

    return "".join(s)


def besedilo(tvit):
    this= []
    notime = False
    for črka in tvit:
        if notime == True  :
            this.append(črka)
        if črka== ":":
            notime = True
    for all in this:
        if all == " ":
            this.remove(all)
            break

    return "".join(this)

def zadnji_tvit(tviti):
    tweets= {}
    for tvit in tviti:
        tweets[avtor(tvit)] = besedilo(tvit)

    return tweets

def prvi_tvit(tviti):
    tweets= {}
    for tvit in tviti:
        if avtor(tvit) not in tweets:
            tweets[avtor(tvit)] = besedilo(tvit)

    return tweets

def prestej_tvite(tviti):
    counter= {}
    for tvit in tviti:
        if avtor(tvit) not in counter:
            i= 0
            counter[avtor(tvit)]= i+1
        else:
            counter[avtor(tvit)]= int(counter[avtor(tvit)])+ 1

    return counter

def omembe(tviti):
    mention= {}
    for tvit in tviti:
        if avtor(tvit) in mention.keys () :
            mention[avtor(tvit)] += (se_zacne_z(tvit, "@" ))
        else:
            mention[avtor(tvit)]=(se_zacne_z(tvit , "@" ))

    return mention


def neomembe(ime, omembe):

    s=[]
    z=[]

    for key , imena in omembe.items():
        if key != ime and key not in s:
            s.append(key)

        else:
            z+=(imena)
    for all in z:
        for to in s:
           if to in z:
               s.remove(to)






    return s


def se_poznata(ime1, ime2, omembe):

    for key, drugo in omembe.items():
        if key == ime1 and ime2 in omembe[key]:
            return True
            break
    for key, drugo in omembe.items():
        if key == ime2 and ime1 in omembe[key]:
            return True
            break

    return False


def hashtagi(tviti):
    s={}
    h=[]
    for tvit in tviti:
        tole = se_zacne_z(tvit, "#")
        h.extend(tole)
    h= unikati(h)

    for tag in h:
        for tvit in tviti:
            if tag in tvit:
                if tag in s.keys():
                    s[tag].append(avtor(tvit))
                else:
                    s.update({tag:[avtor(tvit)]})
    for tag in h:
        s[tag].sort()



    return s





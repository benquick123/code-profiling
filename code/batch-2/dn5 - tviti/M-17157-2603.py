
# coding: utf-8

# In[20]:

#1)prejme seznam nekih stvari in kot rezultat vrne nov seznam, v katerem se vsak element pojavi le enkrat. Vrstni red v
#rezultat naj bo enak vrstnemu redu prvih pojavitev v podanem seznamu. Klic unikati([1, 3, 2, 1, 1, 3, 2]) mora vrniti
#[1, 3, 2].
def unikati(s):
    l = []
    for num in s:
        set(s)
        l.append(set(s))
        return l        


# In[10]:

unikati([1, 3, 2, 1, 1, 3, 2])


# In[314]:

#2)vrne ime avtorja podanega tvita. Klic avtor("ana: kdo so te @berta, @cilka, @dani? #krneki") vrne "ana".
def avtor(tvit):
    a = ""
    for w in tvit.split():
        b = tvit.split()
        if w == b[0]:
            a = b[0]
            a = a.replace(":","")
            return a


# In[317]:

avtor("ana: kdo so te @berta, @cilka, @dani? #krneki")


# In[316]:

tvit = "ana: kdo so te @berta, @cilka, @dani? #krneki"


# In[35]:

tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


# In[88]:

#3)prejme seznam tvitov in vrne seznam vseh njihovih avtorjev. Vsak naj se v seznamu pojavi le enkrat; vrstni red naj bo enak
#vrstnemu redu prvih pojavitev. Če funkcijo pokličemo z gornjim seznamom tvitov, mora vrniti ["sandra", "berta", "ana",
#"cilka", "benjamin", "ema"]. Sandra se pojavi le enkrat, čeprav je napisala dva tvita.
def vsi_avtorji(tviti):
    a = []
    for w in tviti:
        for b in w:
            c = w.split()
            for x in c:
                if x[-1] == ":":
                    t = x.replace(":","")
                    if t not in a:
                        a.append(t)
    return a


# In[89]:

vsi_avtorji(tviti)


# In[23]:

#4)prejme neko besedo in vrne to besedo brez vseh ne-alfanumeričnih znakov (to je, znakov, ki niso črke ali števke) na začetku
#in koncu. Če pokličemo izloci_besedo("!%$ana---"), mora vrniti "ana". Če pokličemo izloci_besedo("@janez-novak!!!"), vrne
#"janez-novak" (in ne "janeznovak"!). Namig: strip() tule morda ne bo preveč uporaben. Pač pa v dokumentaciji Pythona
#preverite, kaj dela metoda isalnum. Potem nalogo rešite tako, da odstranjujte prvi znak besede, dokler ta ni črka. In potem
#na enak način še zadnjega. Kako besedi odstranimo znak, pa boste - če se ne boste spomnili sami - izvedeli v zapiskih o
#indeksiranju.


# In[ ]:
def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1:]
    while beseda[-1].isalnum() == False:
        beseda = beseda[:-1]
    return beseda





# In[ ]:




# In[61]:

#5)prejme nek tvit in nek znak c. Vrniti mora vse tiste besede iz tvita, ki se začnejo s podanim znakom c. Pri tem mora od
#besed odluščiti vse nealfanumerične znake na začetku in na koncu. Klic se_zacne_z("sandra: @berta Ne maram #programiranje1
##krneki", "#") vrne ["programiranje1", "krneki"].


# In[391]:

def se_zacne_z(tvit, c):
    l = []
    a = tvit.isalnum()
    for w in tvit.split():
        if a != True:
            if w.isalnum() != True:
                if w[0] == "#":
                    w = w.replace("#","")
                    if w not in l:
                        l.append(w)
    return l


# In[392]:

se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#")


# In[401]:

#Popravi:
#6)je podobna prejšnji, vendar prejme seznam tvitov in vrne vse besede, ki se pojavijo v njih in se začnejo s podano črko.
#Poleg tega naj se vsaka beseda pojavi le enkrat. Če pokličemo zberi_se_zacne_z(tviti, "@") (kjer so tviti gornji tviti),
#vrne ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana']. Vrstni red besed v seznamu je enak vrstnemu redu njihovih
#pojavitev v tvitih.
tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


# In[398]:

def zberi_se_zacne_z(tviti, c):
    l = []
    a = tvit.isalnum()
    for w in tvit.split():
        if a != True:
            if w.isalnum() != True:
                if w[0] == "@":
                    w = w.replace("@","")
                    if w not in l:
                        l.append(w)
    return l


# In[400]:

zberi_se_zacne_z(tviti, "@")


# In[272]:

#7)vrne vse besede v tvitih, ki se začnejo z @. Če ji podamo gornje tvite, mora vrniti ['sandra', 'berta', 'cilka', 'dani',
#'benjamin', 'ana'].
def vse_afne(tviti):
    a = []
    for w in tviti:
        for x in w:
            c = w.split()
            for b in c:
                if "@" in b:
                    b = b.replace("@","")
                    if b not in a:
                        a.append(b)
    return a        


# In[273]:

vse_afne(["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"])


# In[368]:

#8)Za gornje tvite vrne ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'].
def vsi_hashtagi(tviti):
    s = []
    for w in tviti:
        for l in w.split():
            c = w.split()
            for a in c:
                if a[0] == "#":
                    a = a.replace("#","")
                    if a not in s:
                        s.append(a)
    return s


# In[369]:

vsi_hashtagi(["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"])


# In[ ]:

#9)vrne po abecedi urejen seznam vseh oseb, ki nastopajo v tvitih - bodisi kot avtorji, bodisi so omenjene v tvitih.
#Vsaka oseba naj se pojavi le enkrat. Za gornje tvite funkcija vrne ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema',
#'sandra'].
def vse_osebe(tviti):
    s = []
    z = []
    for w in tviti:
        for l in w:
            c = w.split()
            for x in c:
                if x[0] == "@":
                    t = x.replace("@","")
                    set(t)
                    s.append(t)
                if x[-1] == ":":
                    t = x.replace(":","")
                    set(t)
                    s.append(t)
    for y in s:
        if y not in z:
            z.append(y)
    return z


# In[ ]:

vse_osebe(["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"])


# In[ ]:




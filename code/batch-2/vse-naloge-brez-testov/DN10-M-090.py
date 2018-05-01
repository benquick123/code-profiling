#OBVEZNI DEL

def premozenje(oseba, denar): #pove koliko denarja imajo člani rodbine podane oseb
    ves_denar = denar[oseba] #zabeleži premoženje 'osebe'
    for otrok in otroci[oseba]:
        ves_denar += premozenje(otrok, denar) #in prišteje denar vseh članov pod 'osebo' (gre čez vse veje drevesa)
    return ves_denar

def najbogatejsi(oseba, denar): #vrne terko najbogatejše osebe in količino njenega denarja
    najjaci = oseba #predpostavimo, da je 'oseba' najbogatejša
    kes = denar[oseba]
    for otrok in otroci[oseba]: #gremo čez vse člane
        otrok_kes = najbogatejsi(otrok, denar)[1] #in gledamo njihov denar
        if otrok_kes > kes: #če imajo več denarja, kot trenutni najbogatejši
            najjaci = najbogatejsi(otrok, denar)[0] #si jih zapomnimo
            kes = otrok_kes
    return (najjaci, kes)


#DODATNI DEL

def uravnotezeni(oseba, denar): #rodbina osebe je uravnotežena, če imajo rodbine vseh njenih otrok enako denarja in so tudi same uravnotežene
    kes = []
    for otrok in otroci[oseba]: #ker nas zanimajo le otroci osebe (ne tudi vnuki, itd.)
        kes.append(premozenje(otrok, denar)) #lahko v seznam vstavimo premoženja rodbin otrok
    for x, y in zip(kes, kes[1:]): #in primerjamo njihovo enakost
        if x != y:
            return False
    return True

def neuravnotezeni(oseba, denar): #vrne ime osebe, ki ima neuravnoteženo rodbino (njeni otroci niso enako premožni)
    for prvi in otroci[oseba]:
        for drugi in otroci[prvi]:
            for tretji in otroci[drugi]:
                for cetrti in otroci[tretji]:
                    for peti in otroci[cetrti]:
                        if not uravnotezeni(peti, denar): #ker je max 5 generacij, se sprehodi od spodnje veje navzgor
                            return peti
                    if not uravnotezeni(cetrti, denar): #in pregleduje kdo je prvi neuravnotežen
                        return cetrti
                if not uravnotezeni(tretji, denar):
                    return tretji
            if not uravnotezeni(drugi, denar):
                return drugi
        if not uravnotezeni(prvi, denar):
            return prvi
    if not uravnotezeni(oseba, denar):
        return oseba
    return None #če so vsi uravnoteženi, vrne None (slaba rešitev)
    '''for otrok in otroci[oseba]: #preveri otroke
        if not uravnotezeni(otrok, denar): #če kakšen ni uravnotežen
            return neuravnotezeni(otrok, denar) #ponovi postopek za njegove otroke (itd. po drevesu)
    if uravnotezeni(oseba, denar):  #če so vsi otroci ur., preveri ali je oseba uravnotežena
        return None #če je, vrne None (noben neuravnotežen)
    return oseba #drugače pomeni, da je oseba neuravnotežena in jo vrne'''



###############################
#TESTI (ne spreminjaj)

otroci = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}



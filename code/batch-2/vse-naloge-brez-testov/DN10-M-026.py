'''
    Opis: vaje z rekurzijo (premoženje Novakovih)
    Avtor: Blaž Kumer
    Datum: 19. 12. 2017
'''





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


def premozenje(oseba,denar):
    return sum(premozenje(otrok,denar) for otrok in otroci[oseba]) + denar[oseba]


def najbogatejsi(oseba,denar):
    return max([(oseba,denar[oseba])] + [najbogatejsi(otrok,denar) for otrok in otroci[oseba]], key=lambda ter:ter[1])

def vsota(oseba, denar):
    return sum(vsota(otrok,denar) for otrok in otroci[oseba]) + denar[oseba]

def uravnotezeni(oseba,denar):
    return all(vsota(otroci[oseba][i],denar)==vsota(otroci[oseba][i+1],denar) for i in range(len(otroci[oseba])-1))

def neuravnotezeni(oseba,denar):
    ali=uravnotezeni(oseba,denar)
    if not ali:
        return oseba
    else:
        for otrok in otroci[oseba]:
            x= neuravnotezeni(otrok,denar)
            if x !=None:
                return x




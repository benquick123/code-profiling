
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

def premozenje(oseba, denar):
    price=0

    for otrok in otroci[oseba]:
        price= price+premozenje(otrok,denar)

    dediscina=price+denar[oseba]
    return dediscina

def najbogatejsi(oseba, denar):
    money= (oseba, denar[oseba])           #ta prvi
    print(money)
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok,denar)   #gre otroka čez --> naslednje generacije

        if naj[1] > money[1]:
            money=naj



    return money







# rekurzija pomeni da kliče samo sebe
# to dosežem tako da nekaj, nardi; pol pa samo sebe pokliče in spet to nardi in tako v nedogled
# če hočem pogledat kolko denarja ma rodbina:
# - prištejem denar osebe in pokličem funkcijo za vse otroke te osebe
# pri rekurzivnih funkcijah seznamov gledam prvi element in vse ostale
# torej če hočem najt najbogatejšega člana RODBINE in njegovo ime
# tu me zanima al sm najbogatejši js, al je kdo od mojih otrok bogatejši od mene

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
    return denar[oseba] + sum([premozenje(otrok, denar) for otrok in otroci[oseba]])

def najbogatejsi(oseba, denar):
    clovek = oseba
    najvecja = denar[oseba]
    for otrok in otroci[oseba]:
        otrokovaD = najbogatejsi(otrok,denar)
        if otrokovaD[1] > najvecja:
            najvecja = otrokovaD[1]
            clovek = otrok
    return (clovek, najvecja)
#naredi v eni vrstici

def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    else:
        for otrok in otroci[oseba]:
            s = [premozenje(otrok, denar)]
            #problem ko je len(s)-1 = 0
            if len(s) == 1:
                uravnotezeni(otrok, denar)
            else:
                if s[0] == sum(s[1:])/(len(s)-1) and uravnotezeni(otrok,denar):
                 return True





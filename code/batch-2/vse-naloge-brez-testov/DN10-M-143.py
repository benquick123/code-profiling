

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
    premoz = []
    potomci = []
    for child in otroci[oseba]:
        potomci += [child]
    for person in potomci:
        if otroci[person] != []:
            potomci += otroci[person]
    for person in potomci:
        premoz.append(denar[person])
    return sum(premoz)+denar[oseba]

def potomstvo(oseba):
    potomci = []
    for child in otroci[oseba]:
        potomci += [child]
    for person in potomci:
        if otroci[person] != []:
            potomci += otroci[person]
    return(potomci)

def premoznost(oseba,denar):
    premoz = []
    potomci = potomstvo(oseba)
    for person in potomci:
        premoz.append(denar[person])
    return premoz

def najbogatejsi(oseba,denar):
    izpis = (oseba, denar[oseba])
    potomci=potomstvo(oseba)
    premozenje=premoznost(oseba,denar)
    index=0
    max=denar[oseba]
    for i,x in enumerate(potomci):
        if premozenje[i] > max :
            max=denar[x]
            index=i
            izpis = (potomci[i], premozenje[i])
        elif premozenje[i] >= max:
            max=denar[x]
            index=i
            izpis =(potomci[i],premozenje[i])
    return izpis


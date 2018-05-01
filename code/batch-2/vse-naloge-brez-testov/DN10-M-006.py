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
    #drnar od vseh skupi v rodbini
    #if (oseba, denar[oseba]) is not None:
    d = denar[oseba]
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) is not None:
            d = d + premozenje(otrok, denar)
    return d

def najbogatejsi(oseba, denar):
    #terka najbogatejsa oseba in njen dnar
    naj = denar[oseba]
    najos = oseba
    for otrok in otroci[oseba]:
        if denar[otrok] > naj:
            najos = otrok
            naj = denar[otrok]
    return (najos, naj)


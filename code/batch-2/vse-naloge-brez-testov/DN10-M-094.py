
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
    a = denar[oseba]
    for i in otroci[oseba]:
        a += premozenje(i, denar)
    return a

def najbogatejsi(oseba, denar):
    a = oseba
    b = denar[oseba]
    for i in otroci[oseba]:
        if najbogatejsi(i, denar)[1] > b:
            b = najbogatejsi(i, denar)[1]
            a = najbogatejsi(i, denar)[0]
    return (a, b)












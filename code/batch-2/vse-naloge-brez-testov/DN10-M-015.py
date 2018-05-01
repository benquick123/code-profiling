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
    cash = []
    s = []
    for otrok in otroci[oseba]:
        s += [otrok]
    for osebek in s:
        if otroci[osebek] != []:
            s += otroci[osebek]
    for osebek in s:
        cash.append(denar[osebek])
    return sum(cash, denar[oseba])

def najbogatejsi(oseba, denar):
    max_cash = (oseba, denar[oseba])
    for a in otroci[oseba]:
        trenutno = najbogatejsi(a, denar)
        if trenutno[1] > max_cash[1]:
            max_cash = trenutno
    return max_cash




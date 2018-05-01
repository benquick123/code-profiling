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
    s=0
    for otrok in otroci[oseba]:
        s += premozenje(otrok, denar)

    return s+ denar[oseba]

def najbogatejsi(oseba, denar):
    naj_bogatasi=[(oseba, denar[oseba])]
    naj_denar = denar[oseba]
    for otrok in otroci[oseba]:
        cur = najbogatejsi(otrok, denar)
        if cur[0][1] == naj_denar:
            naj_bogatasi = cur + naj_bogatasi
        elif cur[0][1] > naj_denar:
            naj_bogatasi = cur
            naj_denar = cur[0][1]
    return naj_bogatasi


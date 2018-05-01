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
# Obvezna 1:
def premozenje(oseba, denar):
    ves_denar = denar[oseba]
    for otrok in otroci[oseba]:
        pot = premozenje(otrok, denar)
        ves_denar += pot
    return ves_denar

# Obvezna 2:
def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        st = najbogatejsi(otrok, denar)
        if st[1] > naj[1]:
            naj = st
    return naj


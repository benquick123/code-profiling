
def premozenje(oseba, denar):
    zlatniki = 0
    for otrok in otroci[oseba]:
        print(zlatniki, denar[otrok])
        zlatniki += premozenje(otrok, denar)
        print(zlatniki)
    zlatniki += denar[oseba]
    return zlatniki

def najbogatejsi(oseba, denar):
    bogatun = [("", 0)]
    for otrok in otroci[oseba]:
        if denar[otrok] == bogatun[0][1]:
            bogatun.append(najbogatejsi(otrok, denar))
        try :
            if denar[otrok] > bogatun[0][1]:
                bogatun = najbogatejsi(otrok, denar)
        except:
            if denar[otrok] > bogatun[1]:
                bogatun = najbogatejsi(otrok, denar)
    if denar[oseba] == bogatun[0][1]:
        bogatun.append((oseba, denar[oseba]))
    try:
        if denar[oseba] > bogatun[0][1]:
            bogatun = (oseba, denar[oseba])
    except:
        if denar[oseba] > bogatun[1]:
            bogatun = (oseba, denar[oseba])
    return bogatun

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


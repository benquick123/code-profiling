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
    if len(otroci[oseba]) == 0:
        return denar[oseba]
    else:
        sum = denar[oseba]
        for otrok in otroci[oseba]:
            sum += premozenje(otrok, denar)
        return sum


def najbogatejsi(oseba, denar):
    naj = denar[oseba]
    otrok1 = oseba
    if len(otroci[oseba]) == 0:
        return oseba, denar[oseba]
    else:
        for otrok in otroci[oseba]:
            premozenje_otroka = najbogatejsi(otrok, denar)
            if premozenje_otroka[1] > naj:
                otrok1, naj = premozenje_otroka[0], premozenje_otroka[1]
        return otrok1, naj



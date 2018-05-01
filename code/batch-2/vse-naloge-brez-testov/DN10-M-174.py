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
    s = denar[oseba]
    for x in otroci[oseba]:
        s += premozenje(x, denar)
    return s


def najbogatejsi(oseba, denar):
    s = (oseba, denar[oseba])
    for x in otroci[oseba]:
        n = najbogatejsi(x, denar)
        if type(s) == tuple:
            if n[1] > s[1]:
                s = n
            elif s[1] == n[1]:
                list(s).append(n)
        else:
            if s[0][1] < n[1]:
                s = n
    return s



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
    v = 0
    if not oseba in otroci.keys():
        return 0
    if otroci[oseba] == []:
        v += denar[oseba]
        return v
    else:
        v += denar[oseba]
        for i in otroci[oseba]:
            v += premozenje(i, denar)
        return v


def najbogatejsi(oseba, denar):
    max = (oseba, denar[oseba])
    if not otroci[oseba]:
        return (oseba, denar[oseba])
    elif otroci[oseba]:
        for o in otroci[oseba]:
            if denar[o] > denar[oseba]:
                max_n = najbogatejsi(o, denar)
            else:
                continue
            if max[1] < max_n[1]:
                max = max_n
        return max



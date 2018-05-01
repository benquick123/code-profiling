def premozenje(oseba, denar):
    y = 0
    y += denar[oseba]
    for x in otroci[oseba]:
        y += denar[x]
        for z in otroci[x]:
            y+= denar[z]
            for s in otroci[z]:
                y+= denar[s]
                for k in otroci[s]:
                    y+= denar[k]
                    for h in otroci[k]:
                        y+= denar[h]
    return y




def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for x in otroci[oseba]:
        y = najbogatejsi(x, denar)
        if naj[1] < y[1]:
            naj = y
    return  naj


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

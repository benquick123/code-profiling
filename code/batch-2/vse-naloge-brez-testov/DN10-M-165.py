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
    vsota = 0

    for otrok in otroci.get(oseba):
        vsota += premozenje(otrok, denar)

    if oseba in denar:
        # print(vsota + denar.get(oseba))
        return vsota + denar.get(oseba)

def najbogatejsi(oseba, denar):
    richest = [(oseba, denar.get(oseba))]
    for otrok in otroci.get(oseba):
        if (denar.get(najbogatejsi(otrok, denar)[0][0]) > denar.get(richest[0][0])):
            richest = najbogatejsi(otrok, denar)
        elif (denar.get(najbogatejsi(otrok, denar)[0][0]) == denar.get(richest[0][0])):
            richest.append(najbogatejsi(otrok, denar)[0])
    # print(richest)
    return richest

def najbogatejsi(oseba, denar):

    richest = (oseba, denar.get(oseba))

    for otrok in otroci.get(oseba):
        returned = najbogatejsi(otrok, denar)
        if (denar.get(returned[0]) > denar.get(richest[0])):
            richest = returned
        elif (denar.get(returned[0]) == denar.get(richest[0])):
            # print(richest, returned)
            return richest
    # print(richest)

    return richest


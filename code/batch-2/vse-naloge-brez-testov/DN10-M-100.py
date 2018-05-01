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
    money  = denar[oseba]
    for clan in otroci[oseba]:
        money += premozenje(clan, denar)

    return money

def najbogatejsi(oseba, denar):
    max_oseba = oseba
    max_denar = denar[oseba]
    for clan in otroci[oseba]:
        nova_oseba, nov_denar = najbogatejsi(clan, denar)
        if nov_denar > max_denar:
            max_denar = nov_denar
            max_oseba = nova_oseba

    return (max_oseba, max_denar)

def uravnotezeni(oseba, denar):
  return



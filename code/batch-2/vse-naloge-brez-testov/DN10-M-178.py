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
    money_rodbine = denar.get(oseba)

    for otrok in otroci[oseba]:
        money_otroka = premozenje(otrok, denar)
        money_rodbine = money_rodbine + money_otroka

    return money_rodbine

def najbogatejsi(oseba, denar):
    denar_prve_osebe = (oseba, denar[oseba])
    otroki = otroci.get(oseba)

    for otrok in otroki:
        denar_otrok = najbogatejsi(otrok, denar)
        if denar_prve_osebe[1] < denar_otrok[1]:
            denar_prve_osebe = denar_otrok

    return denar_prve_osebe



denar = {
        "Adam": 42,
        "Aleksander": 3,
        "Alenka": 3,
        "Barbara": 37,
        "Cilka": 242,
        "Daniel": 4,
        "Erik": 32,
        "Elizabeta": 8,
        "Franc": 16,
        "Herman": 12,
        "Hans": 55,
        "Jožef": 7,
        "Jurij": 5,
        "Ludvik": 37,
        "Margareta": 20,
        "Matjaž": 142,
        "Petra": 3,
        "Tadeja": 45,
        "Viljem": 55
    }


print(premozenje("Jožef", denar))
print(najbogatejsi("Jurij", denar))




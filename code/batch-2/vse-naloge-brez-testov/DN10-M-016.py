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

def premozenje(oseba, denar):
    gnar = denar.get(oseba)
    gnar_potomcev = 0

    potomci = otroci.get(oseba)

    for potomec in potomci:

        gnar_potomcev = premozenje(potomec, denar)
        gnar = gnar + gnar_potomcev

    return gnar

print(premozenje("Adam", denar))

def najbogatejsi(oseba, denar):
    #dobi denar od te osebe
    #gnar = denar[0]
    #return gnar

    #katera je najbogatejša oseba iz te "rodbine" - zaenkrat ta ki jo dobimo
    max = (oseba, denar[oseba])

    froci = otroci[oseba]
    for otrok in froci:
        max_otrok = najbogatejsi(otrok, denar)
        if (max_otrok[1] > max[1]):
            max = max_otrok


    return max




def uravnotezeni(oseba, denar):
    froci = otroci[oseba]

    denar_froci = 0

    neuravnotezena = 0
    if froci:
        for otrok in froci:

            denar_froci += premozenje(otrok, denar)

    print(denar_froci)
    print(len(froci))

    if len(froci) != 0 and (denar_froci / len(froci)) == denar[froci[0]]:

        return True

    else:

        return False


#print(uravnotezeni("Jožef", denar))

def neuravnotezeni(oseba, denar):
    return 0


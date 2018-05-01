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
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota


def najbogatejsi(oseba, denar):
    naj = oseba
    najd = denar[oseba]
    for otrok in otroci[oseba]:
        if najd < denar[otrok]:
            (naj, najd) = najbogatejsi(otrok, denar)
    return (naj, najd)


print(najbogatejsi('Elizabeta', denar))

def uravnotezeni(oseba, denar):
    pass



def neuravnotezeni(oseba, denar):
    pass



#_________________________________________ TESTI  _________________________________________


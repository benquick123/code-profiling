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







def premozenje(oseba,denar):
    vsota_denarja=denar[oseba] # na začetku je največja vrednost kar prva vrednost
    for ime in otroci[oseba]:
        vsota_denarja= vsota_denarja + premozenje(ime, denar) # uporabimo rekurzijo
    return vsota_denarja

def najbogatejsi(oseba, denar):
    max_denar = denar[oseba] # na začetku je največja vrednost kar prva vrednost
    max_oseba = oseba # na začetku je ime največje vrednosti kar prvo ime
    for ime in otroci[oseba]:
        max= najbogatejsi(ime, denar) # uporabimo rekurzijo
        if max_denar < max[1]: # denar je shranjen na drugem mestu v terki
            max_oseba= max[0] # ime je shranjeno na prvemu mestu v terki
            max_denar= max[1]
    return (max_oseba,max_denar) # funkcija mora vrniti terko





def premozenje(oseba,denar):
    a = denar[oseba]
    for otrok in otroci[oseba]:
        a=a+premozenje(otrok,denar)
    return a














def najbogatejsi(oseba,denar):

    najbogat = oseba
    c = denar[oseba]

    for otrok in otroci[oseba]:
        naj ,u= najbogatejsi(otrok,denar)
        a = denar[otrok]
        b = denar[najbogat]
        if a > b:
            najbogat = naj
            c = a
    print (najbogat)
    return najbogat,c














































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



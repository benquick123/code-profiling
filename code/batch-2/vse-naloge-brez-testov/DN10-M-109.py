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
    vsota= denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok,denar)
    return vsota


def najbogatejsi(oseba, denar):
   najvec = (oseba,denar[oseba])
   for otrok in otroci[oseba]:
       if denar[otrok] > najvec[1]:
           najvec = najbogatejsi(otrok,denar)
   return najvec

#def uravnotezeni(oseba, denar):
#    seznam = set()
#    for otrok in otroci[oseba]:
#        seznam.add(denar[otrok])
#        if uravnotezeni(otrok, denar) == True or len(seznam) == 1:
#            return True
#    if len(seznam) == 1:
#        return True
#    else:
#        return False



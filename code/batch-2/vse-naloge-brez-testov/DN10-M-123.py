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
    xs = [denar[oseba]]
    for otrok in otroci[oseba]:
        xs.append(premozenje(otrok,denar))
    return sum(xs)



def najbogatejsi(oseba,denar):
    najvec_denarja = 0
    #print("oseba: ",oseba)
    #if denar[oseba] > najbolj_bogat:
    obdelani = []
    najbolj_bogat = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] >= (denar[oseba] in najbolj_bogat):
            najbolj_bogat = najbogatejsi(otrok,denar)
            #if int(denar[otrok]) > najvec_denarja:
               # najvec_denarja = denar[otrok]
            #print(najbolj_bogat,"-----1")
    #print(najbolj_bogat,"-----2")
    #print("------------------------------------------------------")
    #print(najvec_denarja)
        #print(otrok,'---',denar[otrok])
    return najbolj_bogat



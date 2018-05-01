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
    cena=0
    for otrok in otroci[oseba]:
        cena+= premozenje(otrok, denar)
    return cena + denar[oseba]

def najbogatejsi(oseba, denar):
    najbogatejsa= (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        max=najbogatejsi(otrok, denar)
        if(max[1]>najbogatejsa[1]):
            najbogatejsa=max
    return najbogatejsa

def uravnotezeni(oseba, denar):
    sum=[]
    for otrok in otroci[oseba]:
        isTrue=uravnotezeni(otrok, denar)
        sum.append(premozenje(otrok, denar))
        if not isTrue:
            return False
    if len(set(sum))<=1:
        return True
    else:
        return False

def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    for otrok in otroci[oseba]:
        isNone = neuravnotezeni(otrok, denar)
        if isNone is not None:
            return isNone
    return oseba

#Moji testi:
#print(uravnotezeni("Elizabeta",{"Adam": 42,"Aleksander": 3,"Alenka": 3,"Barbara": 37,"Cilka": 242,"Daniel": 4,"Erik": 32,"Elizabeta": 8,"Franc": 16,"Herman": 12,"Hans": 55,"Jožef": 7,"Jurij": 5,"Ludvik": 37,"Margareta": 20,"Matjaž": 142,"Petra": 3,"Tadeja": 45,"Viljem": 55}))
#print(neuravnotezeni("Elizabeta",{"Adam": 42,"Aleksander": 3,"Alenka": 3,"Barbara": 37,"Cilka": 242,"Daniel": 4,"Erik": 32,"Elizabeta": 7,"Franc": 16,"Herman": 12,"Hans": 55,"Jožef": 7,"Jurij": 6,"Ludvik": 37,"Margareta": 20,"Matjaž": 142,"Petra": 3,"Tadeja": 45,"Viljem": 55}))

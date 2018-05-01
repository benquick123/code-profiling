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
    pr = 0
    for otrok in otroci[oseba]:
        pr += premozenje(otrok, denar)
    pr += denar[oseba]
    return pr

def najbogatejsi(oseba, denar):
    najvec = oseba,denar[oseba]
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok,denar)[1] > najvec[1]:
            najvec = najbogatejsi(otrok,denar)
    return najvec

def uravnotezeni(oseba, denar):
    if otroci[oseba] == []:
        return True
    prvi = True
    for otrok in otroci[oseba]:
        if uravnotezeni(otrok, denar) == False:
            return False
        if(uravnotezeni(otrok,denar) == True and prvi == True):
            prvi = otrok
        if(prvi != True):
            if premozenje(prvi,denar) != premozenje(otrok,denar):
                return False
    return True

def neuravnotezeni(oseba, denar):
    if otroci[oseba] == []:
        return None
    prvi = True
    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok, denar) != None:
            return neuravnotezeni(otrok, denar)
        if(neuravnotezeni(otrok,denar) == None and prvi == True):
            prvi = otrok
        if(prvi != True):
            if premozenje(prvi,denar) != premozenje(otrok,denar):
                return oseba
    return None



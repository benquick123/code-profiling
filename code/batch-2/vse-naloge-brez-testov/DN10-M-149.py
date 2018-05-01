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

def premozenje(oseba, denar, prvic = True):
    vsota = 0
    if prvic == True: #preverimo ali se izvaja prvič
        vsota+=denar[oseba]
    for otrok in otroci[oseba]:
        vsota+= denar[otrok] + premozenje(otrok,denar,prvic = False) #povemo, da se NE izvaja prvič
    return vsota

def najbogatejsi(oseba, denar):

    naj_bogastvo = denar[oseba] #"aktualno" bogastvo
    bogat = oseba   #ime "aktualnega" bogataša
    for otrok in otroci[oseba]:
        najbogatejsi(otrok,denar)
        if denar[otrok] >= naj_bogastvo: #primerjava ali ima več kot prejšnji
            naj_bogastvo = denar[otrok] #sprememba aktulanega "naj_bogastva"
            bogat = otrok          #sprememba aktualnega "bogataša
    return bogat, naj_bogastvo


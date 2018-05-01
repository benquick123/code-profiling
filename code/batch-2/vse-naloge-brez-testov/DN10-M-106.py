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
    return denar[oseba]+sum(premozenje(os,denar) for os in otroci[oseba])

def najbogatejsi(oseba,denar):
    maks=denar[oseba]
    maks2=(oseba,denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejsi(otrok,denar)
        d=denar[otrok]
        if d>maks:
            maks2=(otrok,d)
            maks=d
    return maks2

def uravnotezeni(oseba,denar):
    if not otroci[oseba]:
        return True
    else:
        d=premozenje(oseba,denar)-denar[oseba]
        for otrok in otroci[oseba]:
            c=premozenje(otrok,denar)
            if d%c==0:
                uravnotezeni(otrok,denar)
                return True
            else:
                return False

def neuravnotezeni(oseba,denar):
    d=premozenje(oseba,denar)-denar[oseba]
    for otrok in otroci[oseba]:
        c=premozenje(otrok,denar)
        if d%c==0:
            a=neuravnotezeni(otrok,denar)
            if not a==None:
                return a
        else:
            return oseba



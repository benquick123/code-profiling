#PREMOŽENJE NOVAKOVIH

def osebe(oseba):
    seznam_oseb = []
    for otrok in otroci[oseba]:
        seznam_oseb += osebe(otrok) #REKURZIJA
    seznam_oseb.append(oseba)
    return  seznam_oseb

def premozenje(oseba, denar):
    seznam_imena_oseb=osebe(oseba)
    vsota=0

    for ime in seznam_imena_oseb:
        imetje_denarja=denar[ime]
        vsota+=imetje_denarja
    return vsota

def najbogatejsi(oseba, denar):
    seznam_oseb_denarja=[]

    seznam_oseb=osebe(oseba)

    for ime in seznam_oseb:
        imetje_denarja=denar[ime]
        seznam_oseb_denarja.append((ime,imetje_denarja))

    return max(seznam_oseb_denarja, key=lambda oseba:oseba[1])


































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



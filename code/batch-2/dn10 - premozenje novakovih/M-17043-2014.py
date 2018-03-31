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
	d = 0
	for otrok in otroci[oseba]:
		d += premozenje(otrok, denar)
	return d + denar[oseba]

def najbogatejsi(oseba,denar):
	naj = []
	for otrok in otroci[oseba]:
		naj.append(najbogatejsi(otrok, denar)) 
	naj.append((oseba, denar[oseba]))
	return max(naj,key=lambda x: x[1])
	
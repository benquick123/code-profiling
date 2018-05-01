
def premozenje(oseba, denar):
	vsota=denar[oseba]
	for otrok in otroci[oseba]:
		vsota+=premozenje(otrok, denar)
	return vsota


def najbogatejsi(oseba, denar):
	trenutni_max=(oseba, denar[oseba])
	for otrok in otroci[oseba]:
		max_otroka=najbogatejsi(otrok, denar)
		if max_otroka[1]>trenutni_max[1]:
			trenutni_max=max_otroka
	return trenutni_max


def uravnotezeni_(oseba, denar):
	uravnotezenost=[True,denar[oseba]]
	seznam=[] 
	for otrok in otroci[oseba]:
		uravnotezenost_otroka=uravnotezeni_(otrok, denar)
		seznam.append(uravnotezenost_otroka[1])
		uravnotezenost[1]+=uravnotezenost_otroka[1]
		uravnotezenost[0]= uravnotezenost[0] and uravnotezenost_otroka[0]
	uravnotezenost[0]=uravnotezenost[0] and (len(set(seznam))<=1)
	return uravnotezenost

	
def uravnotezeni(oseba, denar):
	return uravnotezeni_(oseba, denar)[0]


def neuravnotezeni_(oseba, denar):
	uravnotezenost=[True,denar[oseba], None]
	seznam=[] 
	for otrok in otroci[oseba]:
		uravnotezenost_otroka=neuravnotezeni_(otrok, denar)
		seznam.append(uravnotezenost_otroka[1])
		uravnotezenost[1]+=uravnotezenost_otroka[1]
		uravnotezenost[0]= uravnotezenost[0] and uravnotezenost_otroka[0]
		if uravnotezenost_otroka[2] is not None:
			return uravnotezenost_otroka
	uravnotezenost[0]=uravnotezenost[0] and (len(set(seznam))<=1)
	if not uravnotezenost[0]:
		uravnotezenost[2]=oseba
	return uravnotezenost


def neuravnotezeni(oseba,denar):
	return neuravnotezeni_(oseba,denar)[2]











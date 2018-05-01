def unikati(s):
	novi_seznam = []
	for element in s:
		if element not in novi_seznam:
			novi_seznam.append(element)
	return novi_seznam

def avtor(tvit):
	return tvit.split(':')[0]

def vsi_avtorji(tviti):
	avtorji = []
	for tvit in tviti:
		avtorji.append(avtor(tvit))
	return unikati(avtorji)

def izloci_besedo(beseda):
	while not beseda[0].isalnum():
		beseda = beseda[1:]
	while not beseda[-1].isalnum():
		beseda = beseda[0:-1]
	return beseda

def se_zacne_z(tvit,c):
	novi_seznam = []
	for beseda in tvit.split():
		if(beseda[0] == c):
			novi_seznam.append(izloci_besedo(beseda))
	return novi_seznam

def zberi_se_zacne_z(tviti, c):
	novi_seznam = []
	for tvit in tviti:
		izlocene_besede = se_zacne_z(tvit,c)
		for beseda in izlocene_besede:
			novi_seznam.append(beseda)
	return unikati(novi_seznam)


def vse_afne(tviti):
	return zberi_se_zacne_z(tviti,'@')

def vsi_hashtagi(tviti):
	return zberi_se_zacne_z(tviti,'#')

def vse_osebe(tviti):
	osebe = []
	for avtor in vsi_avtorji(tviti):
		osebe.append(avtor)
	for afna in vse_afne(tviti):
		osebe.append(afna)
	osebe.sort()
	return unikati(osebe)


def custva(tviti, hashtagi):
	osebe = []
	for tvit in tviti:
		if len([ element for element in se_zacne_z(tvit,'#') if element in hashtagi ]) > 0:
			#se_zacne_z(tvit,'#') in hashtagi:
			osebe.append(avtor(tvit))
	osebe.sort()
	return unikati(osebe)

def se_poznata(tviti, oseba1, oseba2):
	for tvit in tviti:
		if avtor(tvit) == oseba1 and len([ element for element in se_zacne_z(tvit,'@') if element == oseba2 ]) > 0:
			return True
		elif avtor(tvit) == oseba2 and len([ element for element in se_zacne_z(tvit,'@') if element == oseba1 ]) > 0:
			return True
	return False


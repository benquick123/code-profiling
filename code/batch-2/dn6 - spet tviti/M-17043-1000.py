def unikati(s):
	newList = []
	for neki in s:
		if neki not in newList:
			newList.append(neki)
	return newList

def avtor(tvit):
	return tvit.split(" ")[0][:len( tvit.split(" ")[0] )-1]
	
def vsi_avtorji(tviti):
	return unikati([avtor(a) for a in tviti])

def izloci_besedo(beseda):
	while(not beseda[:1].isalnum()):
		beseda = beseda[1:]

	while(not beseda[len(beseda)-1:].isalnum()):
		beseda = beseda[:-1]
		
	return beseda

def se_zacne_z(tvit, c):
	return [izloci_besedo(beseda) for beseda in tvit.split(" ") if beseda[:1] == c]

def zberi_se_zacne_z(tviti, c):
	l = []
	for tvit in tviti:
		l += se_zacne_z(tvit, c)
	return unikati(l)
	
def vse_afne(tviti):
	return zberi_se_zacne_z(tviti,"@")
	
def vsi_hashtagi(tviti):
	return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
	l = []
	l += vsi_avtorji(tviti)
	l += vse_afne(tviti)
	return sorted(list(set(l)))
	
def besedilo(tvit):
	return tvit[len(avtor(tvit))+2:]
	
def zadnji_tvit(tviti):
	d = {}
	for tvit in tviti:
		d[avtor(tvit)] = besedilo(tvit)
	return d
	
def prvi_tvit(tviti):
	d = {}
	for tvit in tviti:
		if avtor(tvit) not in d:
			d[avtor(tvit)] = besedilo(tvit)
	return d
	
def prestej_tvite(tviti):
	d = {}
	for tvit in tviti:
		if avtor(tvit) not in d:
			d[avtor(tvit)] = 1
		else:
			d[avtor(tvit)] += 1
	return d
	
def omembe(tviti):
	d = {}
	for tvit in tviti:
		if avtor(tvit) not in d:
			d[avtor(tvit)] = []
		omembe = se_zacne_z(tvit, "@")
		if len(omembe) != 0:
			if len(d[avtor(tvit)]) == 0:
				d[avtor(tvit)].append(omembe[0])
				for o in omembe:
					if o not in d[avtor(tvit)]:
						d[avtor(tvit)].append(o)
			else:
				for o in omembe:
					if o not in d[avtor(tvit)]:
						d[avtor(tvit)].append(o)
	return d
	
def neomembe(ime, omembe):
	neo = []
	for key, value in omembe.items():
		if key not in omembe[ime] and key != ime:
			neo.append(key)
	return neo
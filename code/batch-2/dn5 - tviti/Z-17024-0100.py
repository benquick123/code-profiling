

tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

# def unikati(s):
# 	nov_seznam=[]
# 	for e in s:
# 		dodaj_v_nov_seznam=True
# 		for f in nov_seznam:
# 			if e==f:
# 				dodaj_v_nov_seznam=False
# 				break
# 		if dodaj_v_nov_seznam:
# 			nov_seznam.append(e)
# 	return nov_seznam

def unikati(s):
	nov_seznam=[]
	for e in s:
		if e not in nov_seznam:
			nov_seznam.append(e)
	return nov_seznam

print(unikati([1,3,2,1,1,3,2]))


def avtor(tvit):
	return tvit.split(':')[0]

print(avtor("marta: kdo so te @berta, @cilka, @dani? #krneki"))


def vsi_avtorji(tviti):
	return unikati([avtor(e) for e in tviti])
	#return unikati(list(map(avtor,tviti)))

print(vsi_avtorji(tviti))


def izloci_besedo(beseda):
	a=-1
	b=-1
	for i, e in enumerate(beseda):
		if e.isalnum():
			a=i
			break
	if a == -1:
		return ''
	for i, e in enumerate(beseda[::-1]):
		if e.isalnum():
			b=i
			break
	dejanski_index_b=len(beseda)-1-b
	return beseda[a:dejanski_index_b+1]


print(izloci_besedo("#programiranje1"))


def se_zacne_z(tvit, c):
	return [izloci_besedo(e) for e in tvit.split(' ') if e[0]==c]

print(se_zacne_z("sandra: @berta Ne maram ##krompirja #programiranje1 #krneki", "#"))


def zberi_se_zacne_z(tviti, c):
	seznam_seznamov = [se_zacne_z(e, c) for e in tviti]
	return unikati([e for seznam in seznam_seznamov for e in seznam])

print(zberi_se_zacne_z(tviti, '@'))


def vse_afne(tviti):
	return zberi_se_zacne_z(tviti, '@')

print(vse_afne(tviti))

def vsi_hashtagi(tviti):
	return zberi_se_zacne_z(tviti, '#')

print(vsi_hashtagi(tviti))

def vse_osebe(tviti):
	return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

print(vse_osebe(tviti))


def custva(tviti, hashtagi):
	seznam_avtorjev=[]
	for tvit in tviti:
		for e in se_zacne_z(tvit, '#'):
			if e in hashtagi:
				seznam_avtorjev.append(avtor(tvit))
				break
	return sorted(unikati(seznam_avtorjev))

print(custva(tviti, ["dougcajt", "krneki"]))


def se_poznata2(tviti, osebaKiPozna, osebaKiJePoznana):
	for tvit in tviti:
		if avtor(tvit) == osebaKiPozna:
			for e in se_zacne_z(tvit, '@'):
				if e == osebaKiJePoznana:
					return True
	return False

def se_poznata(tviti, oseba1, oseba2):
	return se_poznata2(tviti, oseba1, oseba2) or se_poznata2(tviti, oseba2, oseba1)

print(se_poznata(tviti, 'berta', 'ana'))



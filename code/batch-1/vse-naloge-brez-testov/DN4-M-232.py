from math import sqrt

def koordinate(ime, kraji):
	for kraj_ime, kraj_x, kraj_y in kraji:
		if ime == kraj_ime:
			return (kraj_x, kraj_y)
	return None

def razdalja_koordinat(x1, y1, x2, y2):
	return sqrt( (x2-x1)**2 + (y2-y1)**2 )

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
	kraji_v_dometu = []

	for ime_primerjanga_kraja, x, y in kraji:
		if ime != ime_primerjanga_kraja and razdalja(ime,ime_primerjanga_kraja, kraji) <= domet:
			kraji_v_dometu.append(ime_primerjanga_kraja)
	return kraji_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
	ime_najoddaljenesi_kraj = imena[0]
	for ime_kraja in imena:
		if razdalja(ime_kraja,ime, kraji) > razdalja(ime_najoddaljenesi_kraj,ime, kraji):
			ime_najoddaljenesi_kraj = ime_kraja
	return ime_najoddaljenesi_kraj

def zalijemo(ime, domet, kraji):
    kraji_v_dometu = v_dometu(ime,domet,kraji)
    return najbolj_oddaljeni(ime,kraji_v_dometu,kraji)

def presek(s1, s2):
    return [element for element in s1 if element in s2]

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1,domet,kraji),v_dometu(ime2,domet,kraji))


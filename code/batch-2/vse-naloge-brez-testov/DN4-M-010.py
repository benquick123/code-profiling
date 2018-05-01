# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime_kraja==ime:
            return (x,y)
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])


def v_dometu(ime, domet, kraji):
    seznam_krajev_v_dometu = []
    for i, x, y in kraji:
        if abs(razdalja(i, ime, kraji)) <= domet and i != ime:
            seznam_krajev_v_dometu.append(i)
    return seznam_krajev_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):
    max_oddaljen_kraj = ""
    max_razdalja = 0
    for kk in imena:
        r = razdalja(ime,kk,kraji)
        if r > max_razdalja:
            max_razdalja = r
            max_oddaljen_kraj = kk
    return max_oddaljen_kraj


def zalijemo(ime, domet, kraji):
    seznam_krajev_v_dometu = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, seznam_krajev_v_dometu, kraji)


def presek(s1, s2):
    skupni_elementi = []
    for i in s1:
        for x in s2:
            if i == x:
                skupni_elementi.append(i)
    return skupni_elementi


def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)



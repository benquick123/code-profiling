'''
    opis: različne naloge s funkcijami
    avtor: Blaž Kumer
    datum: 6.11.2017

'''



from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj==ime:
            return x,y
    else:
        return None



def razdalja_koordinat(x1,y1,x2,y2):
    razdalja= sqrt((x2-x1)**2+(y2-y1)**2)
    return razdalja



def razdalja(ime1,ime2,kraji):
    xa, ya = koordinate(ime1,kraji)
    xb, yb = koordinate(ime2,kraji)
    razdalja=razdalja_koordinat(xa,ya,xb,yb)
    return razdalja

#OBVEZNE

def v_dometu(ime,domet,kraji):
    s=[]
    for ime1,x,y in kraji:
        if ime1==ime:
            x1=x
            y1=y
            break
    else:
        print("iskanega kraja ni v seznamu")
        return False
    for ime1,x,y in kraji:
        if ime!=ime1:
            razdalja= sqrt((x1-x)**2+(y1-y)**2)
            if razdalja<=domet:
                s.append(ime1)
    return s

def najbolj_oddaljeni(ime,imena,kraji):
    for i,x,y in kraji:
        if i==ime:
            xGL=x
            yGL=y
            break
    else:
        print("iskanega kraja ni v seznamu")
        return False
    s=[]
    for i in imena:
        for j,x,y in kraji:
            if i==j:
                s.append([j,x,y])
                break
    najRaz=0
    najIme=""
    for ime,x,y in s:
        raz=sqrt((x-xGL)**2+(y-yGL)**2)
        if raz>najRaz:
            najIme=ime
            najRaz=raz
    return najIme

def zalijemo(ime,domet,kraji):
    for i,x,y in kraji:
        if i==ime:
            xGL=x
            yGL=y
            break
    else:
        print("iskanega kraja ni v seznamu")
        return False
    najRaz=0
    najIme=""
    for j,x,y in kraji:
        raz = sqrt((x - xGL) ** 2 + (y - yGL) ** 2)
        if raz<=domet:
            if raz>najRaz:
                najRaz=raz
                najIme=j
    return najIme

 #DODATNE

def presek(s1,s2):
    s3=[]
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i]==s2[j]:
                s3.append(s1[i])
    return s3


def skupno_zalivanje(ime1, ime2, domet, kraji):
    for imr,x,y in kraji:
        if imr==ime1:
            x1=x
            y1=y
        if imr==ime2:
            x2=x
            y2=y
    dom1=[]
    dom2=[]
    for ime,x,y in kraji:
        raz1=sqrt((x-x1)**2+(y-y1)**2)
        raz2=sqrt((x-x2)**2+(y-y2)**2)
        if raz1<=domet:
            dom1.append(ime)
        if raz2<=domet:
            dom2.append(ime)
    s3 = []
    for i in range(0, len(dom1)):
        for j in range(0, len(dom2)):
            if dom1[i] == dom2[j]:
                s3.append(dom1[i])
    return s3


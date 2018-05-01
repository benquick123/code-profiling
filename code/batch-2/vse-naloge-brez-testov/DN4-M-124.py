# Tu pišite svoje funkcije:
def v_dometu(ime, domet, kraji):
    mozni = []
    for lol in kraji:
        imee, xcord, ycord = lol
        if imee == ime:
            for ostali in kraji:
                i, prva, druga = ostali
                raz = (((xcord - prva) ** 2) + ((ycord - druga) ** 2)) ** (1 / 2)
                if raz <= domet and i != ime:
                    mozni.append(i);


    return mozni
def najbolj_oddaljeni(ime, imena, kraji):
    naj=0;
    for lol in kraji:
        imee, xcord, ycord = lol
        if imee == ime:
            izbime,xcord,ycord=lol
            for ostali in kraji:
                osti,xxxcord,yyycord=ostali
                for drugi in imena:
                    drugime=drugi
                    if drugime==osti:
                        raz = (((xcord - xxxcord) ** 2) + ((ycord - yyycord) ** 2)) ** (1 / 2)
                        if(raz>naj):
                            tisti=drugime
    return tisti

def zalijemo(ime, domet, kraji):
    for lol in kraji:
        ime, xcord, ycord = lol
        if ime == kraj:
            for ostali in kraji:
                i, prva, druga = ostali
                raz = (((xcord - prva) ** 2) + ((ycord - druga) ** 2)) ** (1 / 2)
                if raz > najraz and raz <= domet:
                    najraz = raz
                    time = i
    return time




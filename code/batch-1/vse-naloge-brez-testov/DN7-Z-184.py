__author__ = 'Dolores'
# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    Args:
        s (int): širina
        v (int): višina

    Returns:
        generator parov polj
    """
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    """
    Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """

    stevilo = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if (x + i, y + j) in mine:
                if i != 0 or j != 0:
                    stevilo=stevilo+1
    return stevilo


def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    koord=(0,0)
    maks=0
    for i in vsa_polja(s,v):
        if sosedov(i[0], i[1], mine) > maks:
            koord = i
            maks = sosedov(i[0], i[1], mine)
    return koord


def brez_sosedov(mine, s, v):
    """
    Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    vsebuje mino.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        set of tuple: polja brez min na sosednjih poljih
    """
    mnozica = set()
    for i in vsa_polja(s, v):
        if sosedov(i[0], i[1], mine) == 0:
            mnozica.add(i)
    return mnozica

def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """
    slovar = {}
    for i in range(9):
        slovar[i]=set()
    for i in vsa_polja(s,v):
        stmin = sosedov(i[0], i[1], mine)
        slovar[stmin].add(i)
    return slovar

########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """
    if len(pot) == 0:
        return 0
    prejsnja = pot[0]
    dolzina=0
    for i in pot:
        dolzina = dolzina + abs(i[0] - prejsnja[0]) + abs(i[1] - prejsnja[1])
        prejsnja = i
    return dolzina

def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je premik varen, `False`, če ni.
    """
    korak = 1
    if (x1 - x0) < 0 or (y1 - y0) < 0:
        korak = -1
    for i in range(x0 ,x1+korak, korak):
        for j in range(y0, y1+korak, korak):
            if (i,j) in mine:
                return False
    return True

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if len(pot) == 0:
        return True
    prejsnja = pot[0]
    for i in pot:
        if not varen_premik(prejsnja[0], prejsnja[1], i[0], i[1], mine):
            return False
        prejsnja = i
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    """
    Vrni koordinate min v podanem polju.

    Niz polje opisuje polje tako, da so vodoravne "vrstice" polja ločene s
    presledki. Prosta polja so označena z znako `.`, mine z `X`.

    Args:
        polje (str): polje

    Returns:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja.
    """
    vrstice=polje.split()
    mine=set()
    s = len(vrstice[0])
    v = len(vrstice)
    for i in range(len(vrstice)):
        premik = 0
        odrezano = vrstice[i][premik:]
        while odrezano.find("X") != -1:
            mine.add((odrezano.find("X")+premik, i))
            premik = premik + odrezano.find("X") + 1
            odrezano = vrstice[i][premik:]

    return (mine, s, v)
########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """
    seznamukazov = ukazi.split()
    x=0
    y=0
    vx=0 #"hitrost" v smeri x
    vy=-1 #"hitrost" v smeri y
    pot = [(0,0)]
    for i in seznamukazov:
        if i == "DESNO":
            if abs(vy) == 1:
                vx = -vy
                vy=0
            else:
                vy=vx
                vx=0
        if i == "LEVO":
            if abs(vy) == 1:
                vx = vy
                vy = 0
            else:
                vy = -vx
                vx = 0
        if i.isnumeric():
            x = x + vx*int(i)
            y = y + vy*int(i)
            pot.append((x,y))
    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    trenutna=None
    niz = ""
    vx = 0 #seznam hitrosti
    vy = -1
    for i in pot:
        if trenutna == None: #Ta funkcija samo nastavi začetno lokacijo, potem se ne izvaja
            trenutna = i
            continue; #Ta stavek prekine trenutno izvedbo for loopa in gre na naslednji i
        pravax = (i[0] - trenutna[0])
        pravay =  (i[1] - trenutna[1])
        if pravax != 0:
            pravax = pravax/abs(pravax)
        if pravay != 0:
            pravay = pravay/abs(pravay)

        zasukov = 0
        while (pravax != vx) or (pravay != vy):
            if abs(vy) == 1:
                vx = -vy
                vy=0
            else:
                vy=vx
                vx=0
            zasukov = zasukov + 1
        for j in range(zasukov):
            niz = niz + "DESNO\n"
        korakov = abs(i[0] - trenutna[0] + i[1] - trenutna[1])
        niz = niz + str(korakov) + "\n"
        trenutna = i
    return niz


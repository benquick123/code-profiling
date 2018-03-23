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
        x (t): koordinata y
        mine (int): koordinata x
        y (inset of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """

    stevilo_sosedov = 0
    for mina in mine:
        for xos in range(-1, 2):
            for yos in range(-1, 2):
                if (xos != 0 or yos != 0): #!= različno od nečesa
                    if mina[0] + xos == x and mina[1] + yos == y:   # če sta oba enaka povečamo
                        stevilo_sosedov = stevilo_sosedov + 1
    return stevilo_sosedov


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
    max_x = 0
    max_y = 0
    max_sosedi = 0
    for vrednost_x in range(0, s): #s je širina polja
        for vrednost_y in range(0, v): #v je dolžina polja
            sosedi = sosedov(vrednost_x, vrednost_y, mine)
            if sosedi > max_sosedi:
                max_x = vrednost_x
                max_y = vrednost_y
                max_sosedi = sosedi
    return (max_x, max_y)

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
    brez_soseda = set() # prazna množica
    for vrednost_x in range(0, s): # s je širina polja
        for vrednost_y in range(0, v): # v je dolžina polja
            if sosedov(vrednost_x, vrednost_y, mine) == 0: #če so vse tri vrednosti enake 0
                brez_soseda.add((vrednost_x, vrednost_y)) # .add doda v množico
    return brez_soseda

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
    slovar_sosedov = {}  #na začetku dekleriran prazen
    for x in range(0, 9): # 0,1,2,3,4,5,6,7,8!!!!
        slovar_sosedov[x] = set() # za vsak x v slovarju naredi ključ od slovarja x, vanj pa naredi prazno množico
    for vrednost_x in range(0, s): # s je širina
        for vrednost_y in range(0, v): # v je dolžina
            slovar_sosedov[sosedov(vrednost_x, vrednost_y, mine)].add((vrednost_x, vrednost_y)) # v slovar sosedov pod ključ da vrednost x, nato pa v množico doda vrednosti x pa y
    return slovar_sosedov

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
    dolzina = 0
    if len(pot) > 0: # dolžina poti mora biti večja od 0
        polje = pot[0]
    else:
        return 0 # če ni vrne rezultat 0
    for vrednost_polja in pot:
        dolzina = dolzina + abs(vrednost_polja[0] - polje[0]) + abs(vrednost_polja[1] - polje[1]) # abs() je absolutna vrednost
        polje = vrednost_polja
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

    if x0 == x1:
        for vrednost_y in range(min(y0, y1), max(y0, y1)+1): # uporaba min(od najmanjsega) pa max (do najvecjega)
            if (x0, vrednost_y) in mine:
                return False # če je potem vrne false (bool)
    else:
        for vrednost_x in range(min(x0, x1), max(x0, x1)+1):
            if (vrednost_x, y0) in mine:
                return False # če je potem vrne false (bool)
    return True # izpis bool vrednosti true

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    if len(pot) > 0: #preverimo če je večje od 0, ker če je 0 je avtomatsko varna
        potka = pot[0]
    else: return True # če je pot enaka 0 je avtomatsko varna
    for vrednost_poti in pot:
        if not varen_premik(potka[0], potka[1], vrednost_poti[0], vrednost_poti[1], mine):
            return False
        potka = vrednost_poti # potka je enaka vrednosti_poti
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
    s = len(polje.split()[0]) # širina polja (split da razdeli elemente, v vrednosti 0)
    v = len(polje.split()) # višina polja (split da razdeli elemente)
    vrstica = 0
    mine = set() # mine deklariramo kot prazna množica
    for vrednost in polje.split(): # polje moramo splitati da se premikamo po elementih
        stolpec = 0
        for mina in vrednost:
            if (mina == "X"):
                mine.add((stolpec, vrstica)) # v množico mine dodamo vrednosti stolpec in vrstica
            stolpec = stolpec + 1
        vrstica = vrstica + 1
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


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """



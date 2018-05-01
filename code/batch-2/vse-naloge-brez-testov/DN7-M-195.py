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

    ##    vsi_sosedi = {(a,b) for a in {x-1, x, x+1} for b in {y-1, y ,y+1}}
    ##    vsi_sosedi = vsi_sosedi - {(x,y)}
    ##    return len(vsi_sosedi & mine)

    return len(mine & {(a, b) for a in {x - 1, x, x + 1} for b in {y - 1, y, y + 1}} - {(x, y)})


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

    ##    koordinata = (0,0)
    ##    max_min = 0
    ##
    ##    for (x,y) in vsa_polja(s,v):
    ##        st_min = sosedov(x,y,mine)
    ##        if st_min > max_min:
    ##            max_min = st_min
    ##            koordinata = (x,y)
    ##
    ##    return koordinata

    ##    pari = []
    ##    for (x,y) in vsa_polja(s,v):
    ##        nov_par = (sosedov(x,y,mine), (x,y))
    ##        pari.append(nov_par)
    ##    # pari = [(3,(1,1)) , (7, (4,5)) , ...]
    ##    max_par = max(pari)
    ##    return max_par[1]

    return max([(sosedov(x, y, mine), (x, y)) for (x, y) in vsa_polja(s, v)])[1]


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

    sosedi = set()  # sosedi min (za vsako mino shranim njene sosede sem noter)
    for (x, y) in mine:
        novi_sosedi = {(a, b) for a in {x - 1, x, x + 1} for b in {y - 1, y, y + 1}} - {(x, y)}
        sosedi = sosedi | novi_sosedi

    return {(x, y) for (x, y) in vsa_polja(s, v)} - sosedi


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

    d = {i: set() for i in range(9)}

    # d = {0:{}, 1:{}, 8:{}}
    for (x, y) in vsa_polja(s, v):
        d[sosedov(x, y, mine)].add((x, y))
    return d


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
    ##    #pot = [(0,0), (0,4), (5,4), (5,3)]
    ##    vsi_premiki = []
    ##    for i in range(len(pot)-1):
    ##        (x0,y0) = pot[i]
    ##        (x1, y1) = pot[i+1]
    ##
    ##        razdalja = abs(x1-x0) + abs(y1-y0)
    ##        vsi_premiki.append(razdalja)
    ##
    ##    return sum(vsi_premiki)

    return sum([abs(pot[i][0] - pot[i + 1][0]) + abs(pot[i][1] - pot[i + 1][1]) for i in range(len(pot) - 1)])


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

    if x1 == x0 and y1 == y0:
        return not (x1, y1) in mine

    elif x0 == x1:
        d = (y1 - y0) // abs(y1 - y0)  # pozitivna ali negativna smer
        korak = 0
        while True:
            y_nov = y0 + d * korak
            if (x0, y_nov) in mine:
                return False
            elif y_nov == y1:
                return True
            else:
                korak += 1


    elif y0 == y1:
        d = (x1 - x0) / abs(x1 - x0)
        korak = 0
        while True:
            x_nov = x0 + d * korak
            if (x_nov, y0) in mine:
                return False
            elif x_nov == x1:
                return True
            else:
                korak += 1


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    return all(
        varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine) for i in range(len(pot) - 1)) if len(
        pot) != 1 else not pot[0] in mine


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

    sez = polje.split()
    v = len(sez)
    s = len(sez[0])
    mine = set()

    for vrstica in range(v):
        for stolpec in range(s):
            if sez[vrstica][stolpec] == 'X':
                mine.add((stolpec, vrstica))
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

    smeri = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    trenutna_smer = 0
    trenutna_pozicija = (0, 0)
    seznam = ukazi.split('\n')
    pot = [(0, 0)]
    for premik in seznam:
        if premik == 'DESNO':
            trenutna_smer = (trenutna_smer + 1) % 4
        elif premik == 'LEVO':
            trenutna_smer = (trenutna_smer - 1) % 4
        else:
            korak = tuple(int(premik) * x for x in smeri[trenutna_smer])
            nova_pozicija = tuple(p + q for p, q in zip(trenutna_pozicija, korak))
            pot.append(nova_pozicija)
            trenutna_pozicija = nova_pozicija
    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """

    ukazi = """"""
    smeri = {(0, -1): 0, (1, 0): 1, (0, 1): 2, (-1, 0): 3}
    trenutna_smer = 0
    for i in range(len(pot) - 1):
        nova = pot[i + 1]
        trenutna = pot[i]
        korak = tuple(p - q for p, q in zip(nova, trenutna))
        dolzina = abs(sum(korak))
        korak_smer = tuple(int(x / dolzina) for x in korak)
        nova_smer = smeri[korak_smer]

        razlika = nova_smer - trenutna_smer
        for j in range(razlika % 4):
            ukazi += 'DESNO\n'
        ukazi += str(dolzina) + '\n'
        trenutna_smer = nova_smer

    return ukazi[:-1]



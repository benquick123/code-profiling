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
    vsi_sosedi = [(x + 1,y),(x - 1,y),(x,y+1),(x,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),(x-1,y-1)]
    st_sosedov = 0
    for mina in mine:
        if mina in vsi_sosedi:
            st_sosedov += 1
    return st_sosedov

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
    najvec = 0
    koordinate = (0,0)
    for j in range(v):
        for i in range(s):
            if sosedov(i,j,mine) > najvec:
                najvec = sosedov(i,j,mine)
                koordinate = (i,j)
    return koordinate

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
    mno = set()
    for j in range(v):
        for i in range(s):
            if sosedov(i,j,mine) == 0:
                mno.add((i,j))
    return mno

def koliko_min(mine,s,v,k):
    mno = set()
    for j in range(v):
        for i in range(s):
            if sosedov(i, j, mine) == k:
                mno.add((i, j))
    return mno

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
    km = {i: set() for i in range(9)}
    for key in km.keys():
        km[key] = koliko_min(mine,s,v,key)
    return km

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
    c = 0
    for i in range(len(pot)-1):
        if pot[i][0] != pot[i+1][0]:
            c += abs(pot[i][0] - pot[i+1][0])
        elif pot[i][1] != pot[i+1][1]:
            c += abs(pot[i][1] - pot[i+1][1])
    return c

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
    dol = dolzina_poti([(x0,y0),(x1,y1)])
    vmesne_koordinate = []
    naj_enak = 0
    enak = 0
    c = 2
    if x0 != x1:
        naj_enak = min(x0,x1)
    elif y0 != y1:
        naj_enak = min(y0,y1)
    if x0 == x1:
        enak = x0
        c = 0
    elif y0 == y1:
        enak = y0
        c = 1
    for i in range(naj_enak,naj_enak+(dol-1)):
        if c == 0:
            vmesne_koordinate.append((enak,i+1))
        elif c == 1:
            vmesne_koordinate.append((i+1,enak))
    vmesne_koordinate.insert(0,(x0,y0))
    vmesne_koordinate.append((x1,y1))
    for koord in vmesne_koordinate:
        if koord in mine:
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
    if len(pot) > 1:
        for i in range(len(pot)-1):
            if not varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine):
                return False
        return True
    else:
        if len(pot) == 0:
            return True
        elif pot[0] in mine:
            return False
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
    se = []
    sezn = polje.split(" ")
    sezn = ' '.join(sezn).split()
    s = len(sezn[0])
    v = len(sezn)
    i = -1
    j = -1
    for vrs in sezn:
        i+=1
        for znak in vrs:
            j+=1
            if znak == "X":
                se.append((j,i))
        j = -1
    return (set(se),s,v)



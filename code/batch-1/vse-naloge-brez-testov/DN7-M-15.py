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
    stevilo = 0
    for xos in range(x-1,x+2):
        for yos in range(y-1,y+2):
            koordinata = (xos, yos)
            #print(koordinata,"---",xos,"---",x,y,"---",yos,"---",mine)
            if koordinata in mine:
                if koordinata != (x,y):
                    stevilo = stevilo + 1
                    #print("stevilo: ",stevilo,"---",koordinata)
                    continue
    #print("Vrnjeno:", stevilo,"--- mine: ",mine)
    return stevilo


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

########################
def najvec_sosedov(mine, s, v):
    polje = (0,0)
    najvec = 0
    for sirina in range(0,s):
        for visina in range(0,v):
            trenutno = sosedov(sirina,visina,mine)
            if trenutno > najvec:
                najvec = trenutno
                polje = (sirina,visina)
                #print("podano: ", s, v, " polje: ", sirina, visina, " ternutno: ", trenutno, " polje: ", polje," mine: ",mine)
                continue
    #print("podano: ", s, v, " polje: ", sirina, visina, " ternutno: ", trenutno, " polje: ", polje, " mine: ", mine)
    return polje

    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """


def brez_sosedov(mine, s, v):
    vrniset = set()
    for sirinabrez in range(0,s):
        for visinabrez in range(0,v):
            trenutnobrez = sosedov(sirinabrez, visinabrez, mine)
            if trenutnobrez == 0:
               #print("koordinatabrez: (",sirinabrez, visinabrez,")")
                vrniset.add((sirinabrez,visinabrez))
                #print(vrniset)
                continue
    #print(vrniset)
    return vrniset


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


def po_sosedih(mine, s, v):
    slovar = {}
    for sosedje in range(0,9):
        vrniset = set()
        for sirinapo in range(0, s):
            for visinapo in range(0, v):
                trenutnopo = sosedov(sirinapo, visinapo, mine)
                if trenutnopo == sosedje:
                    # print("koordinatabrez: (",sirinabrez, visinabrez,")")
                    vrniset.add((sirinapo, visinapo))
                    #print(vrniset)
                    slovar[sosedje] = vrniset
        if len(vrniset) == 0:
            slovar[sosedje] = set()
        #print("dolzinaseta: ",len(vrniset))
    #print(slovar)
    return slovar

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


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzinatabele = len(pot)
    stevilokorakov = 0
    for koraki in range(0,dolzinatabele-1):
        #print(pot[koraki],"---",pot[koraki+1],"---",pot[koraki][0])
        xkorakov = pot[koraki+1][0] - pot[koraki][0]
        ykorakov = pot[koraki+1][1] - pot[koraki][1]
        stevilokorakov = stevilokorakov + (abs(xkorakov)+abs(ykorakov))
        #print("pot: ",pot,"---","ponovitev: ",koraki,"--",stevilokorakov)
    return stevilokorakov

    #print(dolzinatabele)


    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    #print("-------------------------------------------------------------------------------")
    korakix = abs(x1-x0)
    korakiy = abs(y1-y0)
    varno = True
    trenutnapozicija = set()
    #pomik = 0
    if (x0,y0) in mine:
        varno = False
    if (x1,y1) in mine:
        varno = False
    pomik = abs(x1-x0) if abs(x1-x0)>0 else abs(y1-y0)
    #print(x0,y0,x1,y1, " pomik: ",pomik," korakix: ",korakix," korakiy: ",korakiy," mine: ",mine)
    if korakix !=0:
        #print("if koraki x: ",korakix,"-----",range(1,(x1-x0)+1),"------",abs(x1-x0),1)
        if x0 > x1:
            #print("Tukaj_smo: ",range(abs(x1-x0),0,-1))
            for korak in range(abs(x1-x0),0,-1):
            #for korak in range(1,(x1-x0)+1 if abs(x1-x0)>0 else abs(x1-x0),1):
                trenutnapozicija = ((x1+korak),y0)
                #print("Trenutnapozicija_X: ", trenutnapozicija,"---",korak)
                if trenutnapozicija in mine:
                    varno = False
                    continue
        else:
            for korak in range(1,(x1-x0)+1):
            #for korak in range(1,(x1-x0)+1 if abs(x1-x0)>0 else abs(x1-x0),1):
                trenutnapozicija = (x0+korak,y0)
               # print("Trenutnapozicija_X: ", trenutnapozicija)
                if trenutnapozicija in mine:
                    varno = False
                    continue
    else:
        if y0>y1:
            for korak in range(abs(y1-y0),0,-1):
                trenutnapozicija = (x0,y1+korak)
                #print("Trenutnapozicija_Y: ",trenutnapozicija)
                if trenutnapozicija in mine:
                    varno = False
                    break
        else:
            for korak in range(1,(y1-y0)+1):
                trenutnapozicija = (x0,y0+korak)
                #print("Trenutnapozicija_Y: ",trenutnapozicija)
                if trenutnapozicija in mine:
                    varno = False
                    break
    #print("varno: ",varno)
    return varno


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


def varna_pot(pot, mine):
    #print("pot:",pot," mine:",mine)
    #print("dolzina: ",len(pot))
    varnapot = True
    if len(pot) == 0:
        return True
    if len(pot) <2 and pot[0] in mine:
        return False
    elif len(pot) <2 and pot[0] not in mine:
        return True
    for skoki in range(0,len(pot)-1):
        #print("skoki:",skoki)
        #print("prva_koordinata: ",pot[skoki]," druga_koordinata: ",pot[skoki+1])
        #print(pot[skoki][0],pot[skoki][1],pot[skoki+1][0],pot[skoki+1][1])
        varnapot = varen_premik(pot[skoki][0],pot[skoki][1],pot[skoki+1][0],pot[skoki+1][1],mine)
        #print(varnapot)
        if varnapot == False:
            break
    return varnapot
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


########################
# Za oceno 8

def polje_v_mine(polje):
    #print("---------------------------------------\n","polje: >",polje, "<")
    xpozicija = 0
    ypozicija = 0
    xmax = 0
    ymax = 1
    trenutnapozicija = 0
    tabelamin = set()
    #print(polje[0],len(polje))
    for podatek in polje:
        if polje[trenutnapozicija] == " ":
            ypozicija = ypozicija+1
            xpozicija = 0
            ymax = ymax+1
            xmax = 0
        if polje[trenutnapozicija] == ".":
            xpozicija = xpozicija+1
            xmax = xmax+1
        if polje[trenutnapozicija] == "X":
            tabelamin.add((xpozicija,ypozicija))
            xpozicija = xpozicija+1
            xmax = xmax+1
        trenutnapozicija = trenutnapozicija+1
    if polje[len(polje)-1] == " ":
        xmax = xmax+1
        ymax = ymax-1
    #print("trenutnapozicija: ",trenutnapozicija,"lenpolje: ",len(polje), "Vsebina zadnjega :>",polje[len(polje)-1],"<")
    #print("trenutnapozicija: ",trenutnapozicija,"tabelamin: ",tabelamin,"xmax: ",xmax," ymax: ",ymax)
    return (tabelamin,xmax,ymax)

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



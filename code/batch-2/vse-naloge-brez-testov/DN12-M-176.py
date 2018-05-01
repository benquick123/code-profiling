
def st_krozisc(zemljevid):
    st = 0
    for k in zemljevid:
        if len(zemljevid[k]) > 1:
            st += 1
    return st

def unvisited_sosedi(curr, unvisited, zemljevid):
    ret = set()
    for i in zemljevid[curr]:
        if i in unvisited:
            ret = ret.union({i})
    return ret
# Ocena 6.
############################################################
def preberi(ime_datoteke):
    zemljevid = open(ime_datoteke)
    zemljevid_list = zemljevid.read()
    zemljevid_list = zemljevid_list.split('\n')
    zemljevid_dict = dict()
    for i in range(len(zemljevid_list)):
        if(len(zemljevid_list[i]) > 0):
            zemljevid_dict[i + 1] = zemljevid_list[i]
            zemljevid_dict[i + 1] = zemljevid_dict[i + 1].split()
            for j in zemljevid_dict[i + 1]:
                zemljevid_dict[i + 1][zemljevid_dict[i + 1].index(j)] = int(zemljevid_dict[i + 1][zemljevid_dict[i + 1].index(j)])

    for i in zemljevid_dict:
        while zemljevid_dict[i][0] != min(zemljevid_dict[i]):
            tmp = zemljevid_dict[i][0]
            zemljevid_dict[i].pop(0)
            zemljevid_dict[i].append(tmp)

    return zemljevid_dict

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False

    for k in range(len(pot) - 1) :
        if pot[k] not in zemljevid[pot[k + 1]]:
            return False
        if k != 0 and k != len(pot) - 1:
            if len(zemljevid[pot[k]]) <= 1:
                return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    krozisc = st_krozisc(zemljevid)
    pot_med_izhodisci = pot[1:-1]
    if krozisc != len(set(pot_med_izhodisci)):
        return False
    if len(pot_med_izhodisci) > len(set(pot_med_izhodisci)):
        return False
    return True
###################################################################


# Ocena 7
###################################################################
def navodila(pot, zemljevid):
    izvozi = []
    for i in range(1,len(pot) - 1):
        razdalja = zemljevid[pot[i]].index(pot[i - 1]) - zemljevid[pot[i]].index(pot[i + 1])
        razdalja =len(zemljevid[pot[i]]) -  razdalja % len(zemljevid[pot[i]])
        if pot[i - 1] == pot[i + 1]:
            razdalja = 0
        izvozi.append(razdalja)
    return izvozi
###################################################################

# Ocena 8
###################################################################
def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek]
    prejsnje_krozisce = pot[-1]
    pot.append(zemljevid[pot[-1]][0])
    for izvoz in navodila:
        zdajsnje_krozisce = pot[-1]
        if zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) + izvoz > len(zemljevid[zdajsnje_krozisce]) - 1:
            premik = zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) - (len(zemljevid[zdajsnje_krozisce]) - izvoz)
        else:
            premik = zemljevid[zdajsnje_krozisce].index(prejsnje_krozisce) + izvoz
        prejsnje_krozisce = pot[-1]
        pot.append(zemljevid[zdajsnje_krozisce][premik])
    return pot
##################################################################

# Ocena 9
#################################################################

#1.
def sosedi(doslej, zemljevid):
    ret = set()
    for uvoz in doslej:
        for izvoz in zemljevid[uvoz]:
            if (izvoz not in ret) and (izvoz not in doslej):
                ret = ret.union({izvoz})
    return ret

#2.
def razdalja(x, y, zemljevid):
    prevozeno = {x}
    pot = 0
    while y not in prevozeno:
        for i in prevozeno:
            prevozeno = prevozeno.union(zemljevid[i])
        pot+= 1
    return pot
#################################################################

# Ocena 10
#################################################################
def najkrajsa_navodila(x,y, zemljevid):
    node_values = {i:0 for i in zemljevid}
    node_values[x] = 1
    unvisited = {i for i in zemljevid if i != x}

    curr_node = x
    while(y != curr_node):
        for i in unvisited_sosedi(curr_node, unvisited, zemljevid):
            if node_values[i] == 0:
                node_values[i] = node_values[curr_node] + 1
            if node_values[i] > node_values[curr_node] + 1:
                node_values[i] = node_values[curr_node] + 1
        a = [i for i in unvisited if node_values[i] != 0 and i != curr_node]
        min = a[0]
        for i in a:
            if node_values[i] < node_values[min]:
                min = i
        unvisited = unvisited.difference({curr_node})
        curr_node = min
    counter = node_values[y]
    najkrajse = [y]
    for i in range(counter, 0, -1):
        for krozisce in zemljevid[najkrajse[-1]]:
            if node_values[krozisce] == i - 1:
                najkrajse.append(krozisce)
                break
    najkrajse = najkrajse[::-1]
    return navodila(najkrajse, zemljevid)

#################################################################


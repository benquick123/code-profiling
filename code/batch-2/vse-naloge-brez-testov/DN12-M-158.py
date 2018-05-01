def preberi(ime_datoteke):
    d = {}
    f = open(ime_datoteke).readlines()
    for i, line in zip(range(1, len(f) + 1), f):
        d[i] = []
        for x in line.split():
            d[i].append(int(x))
        d[i] = d[i][d[i].index(min(d[i])):] + d[i][:d[i].index(min(d[i]))] 
    return d

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False
    for x in pot[1:-1]:
        if len(zemljevid[x]) == 1:
            return False
    for i, j in zip(pot, pot[1:]):
        if j not in zemljevid[i] or i == j:
            return False
    return True

def hamiltonova(pot, zemljevid):
    for i in zemljevid.keys():
        if len(zemljevid[i]) > 1:
            if pot.count(i) != 1:
                return False
    return mozna_pot(pot, zemljevid)


def navodila(pot, zemljevid):
    return [(zemljevid[pot[i]].index(pot[i+1]) - zemljevid[pot[i]].index(pot[i-1])) % len(zemljevid[pot[i]]) for i in range(1,len(pot) - 1)]

def prevozi(zacetek, navodila, zemljevid):
    res = [zacetek, zemljevid[zacetek][0]]
    for i in navodila:
        res.append(zemljevid[res[-1]] [(zemljevid[res[-1]].index(res[-2]) + i) % len(zemljevid[res[-1]])])
    return res


"""
def sosedi(doslej, zemljevid):
    s = []
    for i in list(doslej):
        s += zemljevid[i]
    return set(s).difference(doslej)
"""

def sosedi(doslej, zemljevid):
    return set([j for i in doslej for j in zemljevid[i]]).difference(doslej)

"""
def razdalja(x, y, zemljevid): #Dijkstra's algorithm
    used = [False] * len(zemljevid.keys())
    used[x - 1] = True
    dist = [100000000000] * len(zemljevid.keys())
    dist[x - 1] = 0
    queue = [x]
    while len(queue):
        for j in zemljevid[queue[0]]:
            if dist[j - 1] > dist[queue[0] - 1] + 1:
                dist[j - 1] = dist [queue[0] - 1] + 1
            if not used[j - 1]:
                queue.append(j)
                used[j - 1] = True
        del queue[0]
    return dist[y - 1]
"""

def razdalja(x, y, zemljevid):
    dist = {x}
    i = 0
    while y not in dist:
        dist = dist.union(sosedi(dist, zemljevid))
        i += 1
    return i


def najkrajsa_navodila(x, y, zemljevid):  #Dijkstra's algorithm (array "used" saves the road)
    used = [-1] * len(zemljevid.keys())
    used[x - 1] = 0
    dist = [100000000000] * len(zemljevid.keys())
    dist[x - 1] = 0
    queue = [x]
    while len(queue):
        for j in zemljevid[queue[0]]:
            if used[j - 1] == -1:
                queue.append(j)
            if dist[j - 1] > dist[queue[0] - 1] + 1:
                dist[j - 1] = dist [queue[0] - 1] + 1
                used[j - 1] = queue[0]
        del queue[0]
    road = [y]
    while y != x:
        road.append(used[y - 1])
        y = used[y - 1]
    return navodila(road[::-1], zemljevid)



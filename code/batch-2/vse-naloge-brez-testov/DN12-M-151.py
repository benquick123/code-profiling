n = 1
def preberi(ime_datoteke):
    dic = {}
    kon = 1
    for file in open(ime_datoteke).readlines():
        dic[kon] = list(map(int, file.split()))[list(map(int, file.split())).index(min(list(map(int, file.split())))):] + list(map(int, file.split()))[:list(map(int, file.split())).index(min(list(map(int, file.split()))))]
        kon = kon + 1
    return dic

def mozna_pot(pot, zemljevid):
    gre = len(pot) - n
    for a in range(0, gre):
        map = zemljevid[pot[a]]
        if pot[a+n] == pot[a] or pot[a+n] not in map or len(zemljevid[pot[0]]) != n or len(zemljevid[pot[len(pot)-n]]) != n:
            return False
    for a in range(n, gre):
        map = zemljevid[pot[a]]
        if n == len(map):
            return False
    else:
        return True

def hamiltonova(pot, zemljevid):
    kon = 2
    team = zemljevid.items()
    lol = len(pot)
    for a, b in team:
        if n != len(b):
            kon = kon + n
    if lol != len(set(pot)) or lol != kon or not mozna_pot(pot, zemljevid):
        return False
    else:
        return True


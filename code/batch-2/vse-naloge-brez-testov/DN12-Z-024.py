
def preberi(ime_datoteke):
    n=1
    slovar={}
    with open(ime_datoteke,"r") as f:
        for vrstica in f:
            vrstica.strip()
            vrednost=[]
            for e in vrstica.split(" "):
                vrednost.append(int(e))
            mesto_min=vrednost.index(min(vrednost))
            vrednost_sort=vrednost[mesto_min:]+vrednost[0:mesto_min]
            slovar[n]=vrednost_sort
            n+=1
    return slovar



def mozna_pot(pot, graf):
    for i in range(len(pot)):
        if pot[i] != pot[-1] and pot[i] not in graf[pot[i+1]]:
            return False
        elif i+1<len(pot) and pot[i] == pot[i+1]:
            return False
        elif len(graf[pot[0]]) != 1 or len(graf[pot[-1]]) != 1:
            return False
        elif i!=0 and i!=len(pot)-1 and len(graf[pot[i]])==1:
            return False
        elif pot[i] != pot[0] and pot[i] != pot[-1] and len(graf[pot[i]])==1:
            return False
    return True

def hamiltonova(pot,zemljevid):
	if not mozna_pot(pot,zemljevid):
		return False
	na_poti=set()
	brez_dodatnih_koncnih=set(a for a in zemljevid if a==pot[0] or a==pot[-1] or len(zemljevid[a])!=1)
	for e in pot:
		if e in na_poti:
			return False
		na_poti.add(e)
	if na_poti!=brez_dodatnih_koncnih:
		return False
	return True


def navodila(pot, graf):
	return [(graf[pot[i+1]].index(pot[i+2])-graf[pot[i+1]].index(pot[i]))%len(graf[pot[i+1]]) for i in range(len(pot)-2)]



def prevozi(zacetek, navodila, graf):
	out=[zacetek,graf[zacetek][0]]
	for e in navodila:
		out.append(graf[out[-1]] [ (graf[out[-1]].index(out[-2])+e)%len(graf[out[-1]])])
	return out


def sosedi(doslej, graf):
	sosedi=set()
	for e in doslej:
		sosedi=sosedi.union(graf[e])
	return sosedi - doslej


def razdalja(x,y,graf):
	cilji={x}
	ze_obiskani=set()
	poteze=0
	if y not in graf:
		return None
	while y not in cilji:
		cilji=sosedi(cilji, graf) - ze_obiskani
		poteze+=1
	return poteze


def pot(x,y,povezave):
  out=[x]
  trenutni=x
  while trenutni!=y:
    trenutni=povezave[trenutni]
    out.append(trenutni)
  return out

def najkrajsa_navodila(x,y,zemljevid):
  obiskani={y}
  povezave={}
  zadnji_obiskani={y}
  while x not in zadnji_obiskani:
    koraki=[(zadnje_mesto,sosedi(set([zadnje_mesto]),zemljevid)-obiskani) for zadnje_mesto in zadnji_obiskani]
    povezave.update({s:lst for lst,step in koraki for s in step})
    zadnji_obiskani={s for _,step in koraki for s in step}
    obiskani=obiskani.union(zadnji_obiskani)
  return navodila(pot(x,y,povezave),zemljevid)



# zemljevid = preberi("zemljevid.txt")
# print(mozna_pot([1, 3, 6, 4, 2, 4, 5, 11, 14, 13, 12], zemljevid))



# zemljevid2 = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
# print(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))


# print(najkrajsa_navodila(15,1,zemljevid))

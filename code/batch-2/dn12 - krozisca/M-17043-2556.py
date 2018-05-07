import unittest
from random import randint
import os

def preberi(ime_datoteke):
	zemljevid = {}
	stevec = 1
	with open(ime_datoteke) as datoteka:
		for vrstica in datoteka:
			min = 999
			minI = 0
			podatki = vrstica.split();
			pStevec = 0
			for podatek in podatki:
				if len(podatek)>3 and podatek[2:] == "\n":
					podatek = podatek[:-2]
				
				if int(podatek) < min:
					min = int(podatek)
					minI = pStevec
				
				if stevec not in zemljevid.keys():
					zemljevid[stevec] = [int(podatek)]
				else:
					zemljevid[stevec].append(int(podatek))
				pStevec+=1
				
			urejeni = []
			for i in range( minI,len(zemljevid[stevec]) ):
				urejeni.append(zemljevid[stevec][i])
			for i in range(0,minI) :
				urejeni.append(zemljevid[stevec][i])
			zemljevid[stevec] = urejeni
			
			stevec+=1
		
	return zemljevid
			
def mozna_pot(pot, zemljevid):
	trenutni = pot[0]
	prvic = True
	
	if len(zemljevid[trenutni]) != 1:
		return False
	
	prejsni = pot[1]
	
	for i in range(0, len(pot)):
		if len(zemljevid[pot[i]]) == 1 and i != 0 and i != len(pot)-1:
			return False
	
		if pot[i] == prejsni:
			return False
		prejsni = pot[i]
		
		if not prvic:
			if trenutni not in zemljevid[pot[i]]:
				return False
		trenutni = pot[i]
		prvic = False
	if len(zemljevid[trenutni]) == 1:
		return True
	return False		
	
def hamiltonova(pot, zemljevid):
	if not mozna_pot:
		return False
		
	zePrevozeni = []
	konci = 0
	
	for cifra in pot:
		if cifra not in zePrevozeni:
			zePrevozeni.append(cifra)
		else:
			return False
	
	for kljuc in zemljevid.keys():
		if len(zemljevid[kljuc]) == 1:
			konci+=1

	if len(zePrevozeni) + konci - 2 == len(zemljevid):
		return True
	else:
		return False

def navodila(pot, zemljevid):
	navodila = []
	for i in range(1, len(pot)-1):
		if (zemljevid[pot[i]].index(pot[i+1]) - zemljevid[pot[i]].index(pot[i-1])) < 0:
			navodila.append( len(zemljevid[pot[i]]) + (zemljevid[pot[i]].index(pot[i+1]) - zemljevid[pot[i]].index(pot[i-1])) )
		else:
			navodila.append( zemljevid[pot[i]].index(pot[i+1]) - zemljevid[pot[i]].index(pot[i-1]) )
	return navodila

def prevozi(zacetek, navodila, zemljevid):
	trenutni = zemljevid[zacetek][0]
	pot = [zacetek,zemljevid[zacetek][0]]
	for premik in navodila:
		pot.append(zemljevid[trenutni][( premik + (zemljevid[trenutni].index(pot[len(pot)-2])) ) % len(zemljevid[trenutni]) ])
		trenutni = pot[len(pot)-1]

	return pot
	
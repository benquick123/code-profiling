def avtor(tvit):
	return tvit.split(':')[0]

def besedilo(tvit):
	return ":".join(tvit.split(':')[1:])[1:]

def zadnji_tvit(tviti):
    seznam = {}
    for tvit in tviti:
        seznam[avtor(tvit)] = besedilo(tvit) 
    return seznam

def prvi_tvit(tviti):
	seznam = {}
	for tvit in tviti:
		if( avtor(tvit) not in seznam):
			seznam[avtor(tvit)] = besedilo(tvit)
	return seznam

def prestej_tvite(tviti):
	seznam = {}
	for tvit in tviti:
		if( avtor(tvit) not in seznam):
			seznam[avtor(tvit)] = 1
		else:
			seznam[avtor(tvit)] = seznam[avtor(tvit)] + 1
	return seznam

def izlociBesedoZPredznakom(besedilo,predznak):
    afne = []
    beseda = ""
    while len(besedilo)>0:
        
        if besedilo[0] == predznak:
            i = 1
            while besedilo[i].isalnum() and i+1 < len(besedilo):
                i = i+1
            if( i+1 == len(besedilo)):
                afne.append(besedilo[1:i+1])
            else:
                afne.append(besedilo[1:i])
            besedilo = besedilo[i:]
        else:
            besedilo = besedilo[1:]
    return afne

def omembe(tviti):
    seznam = {}

    for tvit in tviti:
        if avtor(tvit) not in seznam:
            seznam[avtor(tvit)] = []
        afne = izlociBesedoZPredznakom(besedilo(tvit),'@')
        for afna in afne:
            if(afna not in seznam[avtor(tvit)] and afna != avtor(tvit)):
                seznam[avtor(tvit)].append(afna)

    return seznam


def neomembe(ime, omembe):
    return [element for element in omembe if element not in omembe[ime] and element != ime]

def se_poznata(ime1, ime2, omembe):
    return  ( ime1 in omembe and len([element for element in omembe[ime1] if element == ime2])>0 ) or ( ime2 in omembe and len([element for element in omembe[ime2] if element == ime1])>0 )
            

def hashtagi(tviti):
    seznam = {}

    for tvit in tviti:
        hashtagi = izlociBesedoZPredznakom(tvit,'#')
        for hashtag in hashtagi:
            if hashtag not in seznam:
                seznam[hashtag] = []
            if avtor(tvit) not in seznam[hashtag]:
                seznam[hashtag].append(avtor(tvit))
                seznam[hashtag].sort()
    return seznam


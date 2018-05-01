otroci = {
   "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}

def premozenje(person, money):
    return sum([money[person]] + [premozenje(p, money) for p in otroci[person]])

def najbogatejsi(person, money):
    fortunes = [(person, money[person])]
    for p in otroci[person]:
        fortunes.append(najbogatejsi(p, money))
    return max(fortunes, key = lambda x: x[1])

def uravnotezeni(person, money):
    if len({premozenje(p, money) for p in otroci[person]}) < 2:
        return all(uravnotezeni(p, money) for p in otroci[person])

def neuravnotezeni(person, money):
    for c in otroci[person]:
        if premozenje(c, money) != premozenje(otroci[person][0], money):
            return person
        c = neuravnotezeni(c, money)
        if c: return c


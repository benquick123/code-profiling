#########

def premozenje(person, denar):
    d = denar[person]
    for child in otroci[person]:
        d += premozenje(child, denar)
    return d

###

def najbogatejsi(person, denar):
    m = (person, denar[person])
    for child in otroci[person]:
        if denar[child] > m[1]:
            m = (child, denar[child])
        najbogatejsi(child, denar)
    return m

###

def uravnotezeni(person, denar):
    money = []

    for child in otroci[person]:
        money.append(premozenje(child, denar))

    if money:
        m = money[0]
    else:
        m = 0
    for x in money:
        if x != m:
            return False
    return True

###

def neuravnotezeni(person, denar):
    money = []

    for child in otroci[person]:
        money.append((premozenje(child, denar), (child)))
        neuravnotezeni(child, denar)


    if money:
        m = money[0][0]

    for x, name in money:
        if x != m:
            return child

#########

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



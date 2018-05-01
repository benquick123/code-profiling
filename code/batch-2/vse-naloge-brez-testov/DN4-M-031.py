# Tu pišite svoje funkcije:

def koordinate(name, locations):
    for name2, x, y in locations:
        if name2 == name:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) 

def razdalja(name1, name2, locations):
    return razdalja_koordinat(*koordinate(name1, locations), 
                              *koordinate(name2, locations))

def v_dometu(name, reach, locations):
    return [name2 for name2, x, y in locations 
            if name2 != name and reach >= razdalja(name, name2, locations)]

def najbolj_oddaljeni(name, names, locations):
    farthestLocation = names[0]
    for i in names:
        if razdalja(name, i, locations) > razdalja(name, farthestLocation , locations): 
            farthestLocation = i
    return farthestLocation  

def zalijemo(name, reach, locations):
    return najbolj_oddaljeni(name, 
                             v_dometu(name, reach, locations), 
                             locations)

def presek(s1, s2):
    return list(set(s1).intersection(set(s2)))

def skupno_zalivanje(name1, name2, reach, locations):
    return presek(v_dometu(name1, reach, locations), 
                  v_dometu(name2, reach, locations))










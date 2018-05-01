import math

################################ WARM UP FUNCTIONS ####################################

### Function gives back coordinates of the city we choose.
def koordinate(ime, kraji):
    for imena in kraji:
        for data in imena:
            if ime == data:
                return imena[1], imena[2]

### Function gives back distance between coordinates of two points.
def razdalja_koordinat(x1, y1, x2, y2):
    distance = abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return distance

### Function gives back distance between two cities that we choose.
def razdalja(ime1, ime2, kraji):

### Function uses previous function "koordinate" to provide coordinates of chosen cities.
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)

### When we have coordinates of cities we can use previous function "razdalja_koordinat" to calculate distance between chosen cities.
    distance = razdalja_koordinat(koordinate1[0], koordinate1[1], koordinate2[0], koordinate2[1])
    return distance

################################ OBLIGATORY FUNCTIONS ####################################

### Function gives back list of cities that chosen city can water with selected range.
def v_dometu(ime, domet, kraji):
    seznam = []
    for imena in kraji:

### We make sure that teh city will not try to water itself.
        if imena[0] != ime:

### We use previous function "razdalja" to calculate distances of each city in the dictionary.
            distance = razdalja(ime, imena[0], kraji)

### If distance is in selected range, we append city to the list that this function will return.
            if distance <= domet:
                seznam.append(imena[0])
    return seznam

### Function gives back the name of the city with maximum distance from the selected list of cities in relation to chosen city,
def najbolj_oddaljeni(ime, imena, kraji):

### We set the starting point of maximum distance to 0 and name to none, so we can replace them later with calculated values.
    maksimum = 0
    oddaljen_kraj = None

### In selected list of cities we calculate the distance of each in relation to the chosen city using previous function "razdalja".
    for data in imena:
        distance = razdalja(ime, data, kraji)

### If calculated distance is bigger than selected maximum, we replace the value of maximum with bigger distance and name with the name of the city that has bigger value.
        if distance > maksimum:
            maksimum = distance
            oddaljen_kraj = data
    return oddaljen_kraj

### Function gives back name of most distant city that a chosen city with selected range can water.
def zalijemo(ime, domet, kraji):

### We set the starting point of maximum distance to 0 and name to none, so we can replace them later with calculated values.
    maksimum = 0
    oddaljen_kraj = None

### We determine cities in the selected range of chosen cities with previous function "v_dometu".
    domet = v_dometu(ime, domet, kraji)

### For each city in selected range we calculate distance from chosen city with previous function "razdalja".
    for izbrani in domet:
        distance = razdalja(ime, izbrani, kraji)

### If calculated distance is bigger than selected maximum, we replace the value of maximum with bigger distance and name with the name of the city that has bigger value.
        if distance > maksimum:
            maksimum = distance
            oddaljen_kraj = izbrani
    return oddaljen_kraj

################################ EXTRA FUNCTIONS ####################################

### Function gives back list of elements that are appearing in both of chosen lists.
def presek(s1, s2):
    seznam = []
    for elements in s1:
        if elements in s2:
            seznam.append(elements)
    return seznam


### Function gives back list of cities that can be watered by both of chosen cities with selected range.
def skupno_zalivanje(ime1, ime2, domet, kraji):

### We determine cities in the selected range of chosen cities with previous function "v_dometu".
    domet1 = v_dometu(ime1, domet, kraji)
    domet2 = v_dometu(ime2, domet, kraji)

### We use previous function "presek" to determine cities that are in range of the first chosen city as of the second chosen city.
    skupaj = presek(domet1, domet2)
    return skupaj


################################ UNITTEST ####################################


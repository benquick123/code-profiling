import risar

cas = 0
max_x = 780
max_y = 480
st_krogov = 30
x_koordinate = []
y_koordinate = []
odboj_xx = []
odboj_yy = []
barva = []
premik = 5
for krog in range(0, st_krogov):
    x,y = risar.nakljucne_koordinate()
    x_koordinate.append(x)
    y_koordinate.append(y)
    odboj_xx.append(0)
    odboj_yy.append(0)
    barva.append(risar.nakljucna_barva())
#odboj_y = 0
#odboj_x = 0
#barva = risar.nakljucna_barva()
while cas < 192:
    #risar.krog(x, y, 10, barva, sirina=2)
    for risi in range(0,st_krogov):
        risar.krog(x_koordinate[risi], y_koordinate[risi],10, barva[risi], sirina=2)
    for premikanje in range(0, st_krogov):
        if y_koordinate[premikanje] < max_y and y_koordinate[premikanje] > 0 and odboj_yy[premikanje] == 0:
            y_koordinate[premikanje] += premik
        else:
            y_koordinate[premikanje] -= premik
        if x_koordinate[premikanje] < max_x and x_koordinate[premikanje] > 0 and odboj_xx[premikanje] == 0:
            x_koordinate[premikanje] += premik
        else:
            x_koordinate[premikanje] -= premik
    '''if y < max_y and y > 0 and odboj_y == 0:
        y+= premik
    else:
        y-= premik
    if x < max_x and x > 0 and odboj_x == 0:
        x+= premik
    else:
        x-= premik'''
    cas+= 1
    risar.cakaj(0.001)
    risar.pobrisi()
    for odboj in range(0, st_krogov):
        if y_koordinate[odboj] >= max_y:
            odboj_yy[odboj] = 1
        if y_koordinate[odboj] <= 10:
            odboj_yy[odboj] = 0
        if x_koordinate[odboj] >= max_x:
            odboj_xx[odboj] = 1
        if x_koordinate[odboj] <= 10:
            odboj_xx[odboj] = 0
    '''if y >= max_y:
        odboj_y = 1
    if y <= 10:
        odboj_y = 0
    if x >= max_x:
        odboj_x = 1
    if x <= 10:
        odboj_x = 0'''





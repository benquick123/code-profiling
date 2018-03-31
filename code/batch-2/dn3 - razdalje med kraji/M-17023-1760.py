kraji = [
    ('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75), ('Rateče', -65.04, 70.04),
    ('Ljutomer', 111.26, 71.82), ('Rogaška Slatina', 71.00, 42.00), ('Ribnica', 7.10, -10.50),
    ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32), ('Vinica', 43.81, -38.43),
    ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25), ('Črnomelj', 39.05, -27.93),
    ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54), ('Domžale', -2.34, 31.50),
    ('Hodoš', 120.70, 105.00), ('Škofja Loka', -23.64, 35.07), ('Velike Lašče', 0.00, 0.00),
    ('Velenje', 33.16, 54.29), ('Šoštanj', 29.61, 57.75), ('Laško', 42.60, 33.29),
    ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93),
    ('Radenci', 100.61, 84.00), ('Črna', 15.41, 66.57), ('Radeče', 39.05, 24.57),
    ('Vitanje', 47.36, 57.75), ('Bled', -37.84, 56.07), ('Tolmin', -63.90, 36.75),
    ('Miren', -72.14, 7.04), ('Ptuj', 87.61, 61.32), ('Gornja Radgona', 97.06, 89.25),
    ('Plave', -73.34, 21.00), ('Novo mesto', 37.91, -3.47), ('Bovec', -76.89, 52.50),
    ('Nova Gorica', -69.79, 12.29), ('Krško', 60.35, 14.07), ('Cerknica', -18.89, -3.47),
    ('Slovenska Bistrica', 66.31, 57.75), ('Anhovo', -72.14, 22.78), ('Ormož', 107.71, 61.32),
    ('Škofije', -59.14, -27.93), ('Čepovan', -60.35, 22.78), ('Murska Sobota', 108.91, 87.57),
    ('Ljubljana', -8.24, 22.78), ('Idrija', -43.74, 17.54), ('Radlje ob Dravi', 41.46, 82.32),
    ('Žalec', 37.91, 43.79), ('Mojstrana', -49.70, 64.79),
    ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),
    ('Kočevje', 16.61, -21.00), ('Soča', -69.79, 52.50), ('Ajdovščina', -53.25, 5.25),
    ('Bohinjska Bistrica', -48.49, 47.25), ('Tržič', -22.44, 56.07), ('Piran', -75.69, -31.50),
    ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25), ('Izola', -68.59, -31.50),
    ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03), ('Šentjur', 54.46, 40.32),
    ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00), ('Mislinja', 42.60, 66.57),
    ('Metlika', 48.56, -19.21), ('Žaga', -81.65, 49.03), ('Komen', -63.90, -1.68),
    ('Žužemberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54), ('Vrhnika', -23.64, 14.07),
    ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32), ('Jesenice', -40.19, 64.79),
    ('Kobarid', -74.55, 43.79), ('Portorož', -73.34, -33.18), ('Muta', 37.91, 82.32),
    ('Sežana', -54.39, -13.96), ('Vipava', -47.29, 1.79), ('Maribor', 72.21, 75.28),
    ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78), ('Na Logu', -62.69, 57.75),
    ('Stara Fužina', -52.04, 47.25), ('Motovun', -56.80, -52.50), ('Pragersko', 73.41, 57.75),
    ('Most na Soči', -63.90, 33.29), ('Brestanica', 60.35, 15.75),
    ('Savudrija', -80.44, -34.96), ('Sodražica', 0.00, -6.93),
]

###                 obvezna naloga                  ###

from math import *

ime_kraja = "Litija"
domet = 60

naj_razdalja = 0
naj_kraj = ""
x = 0
y = 0
ime_ustreza = False

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    if t_ime == ime_kraja:
        x = t_x
        y = t_y
        ime_ustreza = True

if not ime_ustreza:
    print ("Seznam krajev ne vkjucuje vnosa", ime_kraja)
    print("Koordinate so bile postavljene na 0,0")

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    razdalja = sqrt( (x - t_x)**2 + (y - t_y)**2 )
    if razdalja <= domet:
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            naj_kraj = t_ime

print(ime_kraja, "je na koordinatah", x, y)
print("Iz kraja", ime_kraja, "lahko zalijemo kraj", naj_kraj, "na razdalji", naj_razdalja)


###                 dodatna naloga                  ###

kraj1 = "Ljubljana"
kraj2 = "Bled"
domet = 30

kraji_v_dosegu_1 = []
kraji_v_dosegu_2 = []

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    if t_ime == kraj1:
        x1 = t_x
        y1 = t_y

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    if t_ime == kraj2:
        x2 = t_x
        y2 = t_y

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    razdalja = sqrt( (x1 - t_x)**2 + (y1 - t_y)**2 )
    if razdalja <= domet and t_ime != kraj1:
        kraji_v_dosegu_1 = kraji_v_dosegu_1 + [t_ime]

for t_kraj in kraji:
    t_ime, t_x, t_y = t_kraj
    razdalja = sqrt( (x2 - t_x)**2 + (y2 - t_y)**2 )
    if razdalja <= domet and t_ime != kraj2:
        kraji_v_dosegu_2 = kraji_v_dosegu_2 + [t_ime]

print("\n\nKraji, ki jih lahko zalivata ", kraj1, "in", kraj2, "hkrati:")
for x in kraji_v_dosegu_1:
    if x in kraji_v_dosegu_2:
        print("-",x)

###                 super extra naloga                 ###


kraj1 = "Koper"
kraj2 = "Maribor"
domet = 30

pot = []
doseg_prejsnega = []
najm_st_korakov = 1000
st_korakov = 0
seznam_poti = []
koraki_do_krajev = []

def rek(pot, r_kraj, doseg_prejsnega, st_korakov):
    pot_x = pot + [r_kraj]
    global seznam_poti
    if r_kraj == kraj2:
        seznam_poti = seznam_poti + [pot_x]
        #print(pot_x)


    ### vrže vn iz rekurzije vse tiste, ki so do trenutnega kraja potrebovale dlje, kot prejšne rekurzije
    global koraki_do_krajev
    st = 0
    for t_kraj in koraki_do_krajev:
        t_ime, t_st = t_kraj
        if r_kraj == t_ime:
            if t_st < st_korakov:
                return 0
            else:
                koraki_do_krajev[st] = (r_kraj, st_korakov)
                break
        st = st + 1
    else:
        koraki_do_krajev = koraki_do_krajev + [(r_kraj, st_korakov)]

    ### vrže vn vse, ki so trenutno naredile več korakov, kot je do sedaj najkrajša pot
    global najm_st_korakov
    if st_korakov >= najm_st_korakov:
        return 0
    else:
        if r_kraj == kraj2:
            najm_st_korakov = st_korakov

    kraji_v_dosegu = []

    for t_kraj in kraji:
        t_ime, t_x, t_y = t_kraj
        if t_ime == r_kraj:
            r_x = t_x
            r_y = t_y

    for t_kraj in kraji:
        t_ime, t_x, t_y = t_kraj
        razdalja = sqrt( (r_x - t_x)**2 + (r_y - t_y)**2 )
        if razdalja <= domet and t_ime != r_kraj and t_ime not in doseg_prejsnega:
            kraji_v_dosegu = kraji_v_dosegu + [t_ime]


    for t_kraj in kraji_v_dosegu:
        if t_kraj not in pot:
            rek (pot_x, t_kraj, kraji_v_dosegu + doseg_prejsnega, st_korakov+1)


rek (pot, kraj1, doseg_prejsnega, st_korakov)

print("\n\n\nIz kraja ", kraj1, "v kraj", kraj2, "najhitreje pridemo v", najm_st_korakov, "korakih.")

st_najk_poti = 0
for p in seznam_poti:
    if len(p) == najm_st_korakov+1:
        st_najk_poti += 1

print("Vseh najkrajsih moznih poti je: ", st_najk_poti,".\n")


for p in seznam_poti:
    if len(p) == najm_st_korakov+1:
        print(p)





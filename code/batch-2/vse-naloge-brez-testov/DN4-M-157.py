
# coding: utf-8

# In[3]:

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

from math import *


# In[1]:

def koordinate(ime, kraji):
    x1 = 0
    y1 = 0
    for kraj in kraji:
        ime1, x1, y1 = kraj
        if ime == ime1:
            return x1, y1


# In[4]:

koordinate("Savudrija",kraji)


# In[5]:

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja


# In[6]:

razdalja_koordinat(0.00,0.00,-80.44, -34.96)


# In[7]:

def razdalja(ime1, ime2, kraji):
    x1=0
    y1=0
    x2=0
    y2=0
    for kraj in kraji:
        ime,x,y = kraj
        if ime1 == ime:
            x1 += x
            y1 += y
        if ime2 == ime:
            x2 += x
            y2 += y
        razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)    
    return "Koordinate:",x1,y1,x2,y2,"Razdalja:",razdalja


# In[8]:

razdalja("Ljubljana","Cerknica",kraji)


# In[13]:

#Obvezni del:

#1. Vrni seznam krajev, ki jih lahko zalije kraj (ime), če ima top z dometom (domet). Kraj ne zaliva sebe.

#2. najbolj_oddaljeni(ime, imena, kraji) prejme ime nekega kraja, seznam imen nekih krajev (imena) in že običajni seznam terk
#z imeni in koordinatami krajev.
#Med kraji v seznamu imena (ne med vsemi kraji, temveč samo med temi!) mora vrniti ime tistega, ki je najbolj oddaljen od kraja
#ime. Če recimo, pokličemo najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji),
#kjer so kraji vsi kraji iz prejšnje naloge, vrne "Maribor", saj je Maribor med temi štirimi kraji najdalj od Ljubljane

#3. zalijemo(ime, domet, kraji) vrne ime najbolj oddaljenega kraja, ki ga lahko zalije kraj ime, če ima top z dometom domet.


# In[66]:

def v_dometu(ime, domet, kraji):
    x1 = 0
    y1 = 0
    x = 0
    y = 0
    razdalja = 0
    
    for kraj in kraji:
        ime1, x1, y1 = kraj
        if ime == ime1:
            print ("Lj:",x1,y1)
            x = x1
            y = y1
            for kraj in kraji:
                ime1, x1, y1 = kraj
                razdalja1 = sqrt((x-x1)**2 + (y-y1)**2)
                if razdalja1 <= domet and ime1 != ime:
                    print ("Od kraja",ime,"je kraj",ime1,"oddaljen",razdalja1,"km.")


# In[67]:

v_dometu("Ljubljana",30,kraji)


# In[33]:

def zalijemo(ime, domet, kraji):
    x=0
    y=0
    razdalja=0
    kraj2 = ""
    for kraj in kraji:
        ime1, x1, y1 = kraj
        razdalja1 = sqrt((x-x1)**2 + (y-y1)**2)
        if ime == ime1:
            x = x1
            y = y1
            print (ime,"Leži na koordinatah",x,y)
            for mesto in kraji:
                ime2, x2, y2 = mesto
                razdalja1 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if razdalja < razdalja1 <= domet:
                    razdalja = razdalja1
                    kraj2 = ime2
            print ("Iz kraja",ime,"lahko zalijemo",kraj2,",na razdalji",razdalja,"metrov.")                   


# In[34]:

zalijemo("Ljubljana",30,kraji)


# In[35]:

imena = ["Domžale", "Kranj", "Maribor", "Vrhnika"]


# In[85]:

def najbolj_oddaljeni(ime, imena, kraji):
    x=0
    y=0
    razdalja=0
    ime4 = ""
    
    for kraj in kraji:
        ime1,x1,y1 = kraj
        if ime == ime1:
            x = x1
            y = y1
            print (ime,"Leži na koordinatah",x,y)
            for mesto in kraji:
                ime2, x2, y2 = mesto
                for ime3 in imena:
                    if ime3 == ime2:
                        razdalja1 = sqrt((x - x2)**2 + (y - y2)**2)
                        if razdalja1 > razdalja:
                            ime4 = ime2
            print (ime4)


# In[86]:

najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji)


# In[ ]:




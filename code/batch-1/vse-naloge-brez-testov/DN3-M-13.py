{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ljubljana je na koordinatah -8.24 22.78\n",
      "Iz kraja  Ljubljana lahko zalijemo Rogaska Slatina na razdalji 29.8165205884\n"
     ]
    }
   ],
   "source": [
    "kraji = [('Brezice', 68.66, 7.04), ('Lenart', 85.20, 78.75), ('Ratece', -65.04, 70.04),\n",
    "         ('Ljutomer', 111.26, 71.82), ('Rogaska Slatina', 71.00, 42.00), ('Ribnica', 7.10, -10.50),\n",
    "         ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32), ('Vinica', 43.81, -38.43),\n",
    "         ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25), ('Crnomelj', 39.05, -27.93),\n",
    "         ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54), ('Domzale', -2.34, 31.50),\n",
    "         ('Hodos', 120.70, 105.00), ('Skofja Loka', -23.64, 35.07), ('Velike Lasce', 0.00, 0.00),\n",
    "         ('Velenje', 33.16, 54.29), ('Sostanj', 29.61, 57.75), ('Lasko', 42.60, 33.29),\n",
    "         ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93),\n",
    "         ('Radenci', 100.61, 84.00), ('Crna', 15.41, 66.57), ('Radece', 39.05, 24.57),\n",
    "         ('Vitanje', 47.36, 57.75), ('Bled', -37.84, 56.07), ('Tolmin', -63.90, 36.75),\n",
    "         ('Miren', -72.14, 7.04), ('Ptuj', 87.61, 61.32), ('Gornja Radgona', 97.06, 89.25),\n",
    "         ('Plave', -73.34, 21.00), ('Novo mesto', 37.91, -3.47), ('Bovec', -76.89, 52.50),\n",
    "         ('Nova Gorica', -69.79, 12.29), ('Krsko', 60.35, 14.07), ('Cerknica', -18.89, -3.47),\n",
    "         ('Slovenska Bistrica', 66.31, 57.75), ('Anhovo', -72.14, 22.78), ('Ormož', 107.71, 61.32),\n",
    "         ('Skofije', -59.14, -27.93), ('Cepovan', -60.35, 22.78), ('Murska Sobota', 108.91, 87.57),\n",
    "         ('Ljubljana', -8.24, 22.78), ('Idrija', -43.74, 17.54), ('Radlje ob Dravi', 41.46, 82.32),\n",
    "         ('Zalec', 37.91, 43.79), ('Mojstrana', -49.70, 64.79),\n",
    "         ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),\n",
    "         ('Kocevje', 16.61, -21.00), ('Soca', -69.79, 52.50), ('Ajdovscina', -53.25, 5.25),\n",
    "         ('Bohinjska Bistrica', -48.49, 47.25), ('Trzic', -22.44, 56.07), ('Piran', -75.69, -31.50),\n",
    "         ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25), ('Izola', -68.59, -31.50),\n",
    "         ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03), ('Sentjur', 54.46, 40.32),\n",
    "         ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00), ('Mislinja', 42.60, 66.57),\n",
    "         ('Metlika', 48.56, -19.21), ('Zaga', -81.65, 49.03), ('Komen', -63.90, -1.68),\n",
    "         ('Zuzemberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54), ('Vrhnika', -23.64, 14.07),\n",
    "         ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32), ('Jesenice', -40.19, 64.79),\n",
    "         ('Kobarid', -74.55, 43.79), ('Portoroz', -73.34, -33.18), ('Muta', 37.91, 82.32),\n",
    "         ('Sezana', -54.39, -13.96), ('Vipava', -47.29, 1.79), ('Maribor', 72.21, 75.28),\n",
    "         ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78), ('Na Logu', -62.69, 57.75),\n",
    "         ('Stara Fuzina', -52.04, 47.25), ('Motovun', -56.80, -52.50), ('Pragersko', 73.41, 57.75),\n",
    "         ('Most na Soci', -63.90, 33.29), ('Brestanica', 60.35, 15.75),\n",
    "         ('Savudrija', -80.44, -34.96), ('Sodrazica', 0.00, -6.93)]\n",
    "from math import *\n",
    "\n",
    "kraj = \"Ljubljana\"\n",
    "domet = 30\n",
    "n = 0\n",
    "kraj2 = ''\n",
    "for mesto in kraji:\n",
    "    ime, x, y = mesto\n",
    "    if ime == kraj:\n",
    "        print kraj, 'je na koordinatah', x, y\n",
    "    for mesto2 in kraji:\n",
    "        razdalja = sqrt((x - y) ** 2 + (n1 - n2) ** 2)\n",
    "    if razdalja < domet and razdalja > n:\n",
    "        n = razdalja\n",
    "        kraj2 = ime\n",
    "print 'Iz kraja ', kraj, 'lahko zalijemo', kraj2, 'na razdalji', n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

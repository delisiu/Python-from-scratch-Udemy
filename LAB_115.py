##Sekcja 8, wykład 115
##1. Zaimportuj moduł math
##2. Oto wzory pozwalające na wykonanie konwersji
##stopni na radiany i radianów na stopnie:
##    1° = (π * rad)/180   
##    1 rad = 180°/π   
##3. Zadeklaruj zmienną degree i przypisz jej wartość 360.
##Wylicz i wyświetl ile to jest 360  stopni
##4. Zmień wartość zmiennej degreee na 45 stopni i powtórz obliczenia
##5. ... ale moduł math ma funkcję radians,
##która wykonuje konwersję stopni na radiany!
##Porównaj wyniki zwracane przez Twoje obliczenia z obliczeniami funkcji radians.
##6. Pizzeria oferuje pizze:
##    small - promień 22 cm, cena, 11.50
##    big - promień 27 cm, cena 15.60
##    family - promień 38cm, cena 22.00
##Zadeklaruj zmienne
##small_pizza_r, big_pizza_r, family_pizza_r oraz small_pizza_price,
##big_pizza_price, family_pizza_price i zapisz w nich w/w wartości.
##7. Oblicz pole powierzchni pizz w metrach kwadratowych
##8. Wyznacz cenę metra kwadratowego pizzy small, big i family
##9. Zobacz jakie inne funkcje są dostępne w module math.
##Możesz w tym celu odwiedzić stronę
##https://docs.python.org/2/library/math.html
##lub wykonać polecenie:
##    math_ls = dir(math) 
##    print(math_ls)

#1
import math

#2
##    1° = (π * rad)/180   
##    1 rad = 180°/π

#3
import math
 
degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
#4
degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')
#5
print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')
#6
small_pizza_r=22/100
big_pizza_r=27/100
family_pizza_r=38/100
small_pizza_price=11.5
big_pizza_price=15.6
family_pizza_price=22
#7
pow_small=math.pi*math.pow(small_pizza_r,2)
pow_big=math.pi*math.pow(big_pizza_r,2)
pow_family=math.pi*math.pow(family_pizza_r,2)
print("Powierzchani pizzy %s wynosi %.2f metrow kwadratowych" % ("small",pow_small))
print("Powierzchani pizzy %s wynosi %.2f metrow kwadratowych" % ("big",pow_big))
print("Powierzchani pizzy %s wynosi %.2f metrow kwadratowych" % ("family",pow_family))
#8
small_pr_m=small_pizza_price/pow_small
big_pr_m=big_pizza_price/pow_big
family_pr_m=family_pizza_price/pow_family
print("Cena metra kwadratowego pizzy pizzy %s wynosi %.2f zł" % ("small",small_pr_m))
print("Cena metra kwadratowego pizzy pizzy %s wynosi %.2f zł" % ("big",big_pr_m))
print("Cena metra kwadratowego pizzy pizzy %s wynosi %.2f zł" % ("family",family_pr_m))

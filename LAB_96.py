##Sekcja 7, wykład 96
##
##ZADANIE 1
##W tym zadaniu obliczysz silnię.
##Silnia  to działanie matematyczne, które dla liczby n wyznacza wartość
##mnożąc przez siebie wszystkie liczby naturalne mniejsze lub równe n.
##Symbol oznaczający silnię to wykrzyknik, np.:
##
##    2! = 1*2 =2
##    3! = 1*2*3 = 6
##    4! = 1*2*3*4 = 24
##https://pl.wikipedia.org/wiki/Silnia
##Zmienna i ma wartość 10.
##Korzystając z pętli for wyznacz wartość silnia i
##ZADANIE 2
##Chcesz wyznaczyć wartości silnia dla liczb od 1 do 10.
##Napisz pętlę for iterującą przez wartości od 1 do 10,
##a w tej pętli for wyznaczaj silnię dla każdej z tych liczb
##ZADANIE 3
##Masz liczbę rzeczowników i przymiotników:
##    list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
##    list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
##Utwórz pętlę for iterującą przez listę rzeczowników
##i zagnieżdżoną w niej pętlę for iterującą przez listę przymiotników.
##Wyświetl wszystkie pary przymiotnik - rzeczownik
#1
i = 10
s=1
for k in range (1,i+1):
    s=s*k
    # s=s*k  to samo s*=k
print(k,"! = ",s*k)
#2
i = 10
s=1
for k in range (1,i+1):
    s=s*k
    # s=s*k  to samo s*=k
    print(k,"! = ",s*k)
#
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
for elem in list_noun:
    for elem2 in list_adj:
        print(elem2,elem)


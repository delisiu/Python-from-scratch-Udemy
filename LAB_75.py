##Sekcja 6, wykład 75
##
##Tym razem pomożemy lekarzom przeprowadzając wstępną analizę:
##czy pacjent ma grypę, czy tylko przeziębienie
##(zakładamy, że pacjentowi coś dolega,
## w tym zadaniu mamy tylko pomóc zdiagnozować czy to jest grypa
## czy przeziębienie):
##1, Utwórz 3 zmienne
##-musclePain - wartość false
##-fever - wartość true
##-weakness - wartość true
##2. Napisz wyrażenie if, które
##-jeśli występuja wszystkie 3 objawy wyświetli komunikat
##"suspiction of influenza"
##-w przeciwnym razie wyświetli "The flu is unlikely"
##3. Napisz wyrażenie if, które:
##-jeśli występuja wszystkie 3 objawy wyświetli komunikat
##"suspiction of influenza"
##-jeśli wystęouje osłabienie (weakness)
##ale nie ma gorączki lub nie ma bólu mięśni to wyświetli "Just take a rest!"
##-w przeciwnym razie wyświetli "you may be cold"
##4. Mężczyźni przeziębienie przechodzą jak grypę...
##dodaj zmienną isMan o wartości true
##5. Napisz wyrażenie if, które:
##-komunikat o grypie wyświetli jeżeli występują wszystkie 3 objawy
##lub co najmniej jeden z nich o ile pacjent jest mężczyzną
##-w pozostałych przypadkach zachowanie ma być jak w  poprzednim przykładzie
##6. Zmieniamy temat.
##Pilot przed wystartowaniem powinien sprawdzić listę kontrolną.
##Właśnie piszesz kod, który odpowiada za wyświetlenie napisu
##"CHECK IS COMPLETED" jeżeli lista kontrolna została już pomyślnie wykonana
##i zamknięta, w przeciwnym razie powinien być wyświetlany komunikat
##"CHECK NOT DONE YET!".
##Zmienna True/False, która zawiera informację o tym czy lista kontrolna
##została już wykonana nazywa sie isCheckCompleted.
##Korzystając z ternary operator przygotuj polecenie if
##wyświetlające odpowiedni komunikat
#1
musclePain = False
fever = False
weakness =  True
#2
print("Suspiction of influenza" if musclePain and fever and weakness else "The flu is unlikely")
#3
if musclePain and fever and weakness:
    print("Suspiction of influenza")
elif weakness and not (fever or musclePain):
    print("Just take a rest!")
else:
    print("You may be cold")
#4
isMan = True
#5
if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("Suspiction of influenza")
elif weakness and not (fever or musclePain):
    print("Just take a rest!")
else:
    print("You may be cold")
#6
isCheckCompleted = False
print ("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")

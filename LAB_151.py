##Sekcja 9, wykład 151
##ZADANIE 1
##Nadal kontynuujemy pracę nad poprzednio tworzonymi funkcjami.
##Funkcja PrintAnimal(animal) wyświetla obrazek
##odpowiadający przekazanemu parametrowi.
##A co jeśli żaden parametr nie zostanie przekazany?
##Obecnie funkcja wyświetli błąd.
##Zmień to. Jeżeli żaden parametr nie został przekazany,
##to parametr animal ma być zainicjowany napisem pustym.
##Po zmianie wywołaj funkcję przekazując parametr lub go opuszczając.
##W przypadku opuszczenia parametru powinien zostać wyświetlony komunikat
##wskazujący na poprawne wartości parametru.
##
##ZADANIE 2
##Funkcja DaysToEndOfYear(year, month, day) z poprzeniego laboratorium
##też wymaga drobnej poprawki
##Jeżeli któryś z parametrów został opuszczony podczas wywołania,
##to należy podstawić rok, miesiąc lub dzień z daty dzisiejszej.
##Przetestuj wywołanie funkcji na różne sposoby
##Uwaga! Ponieważ operacje na dacie trzeba wykonać
##jeszcze przed samą definicją funkcji
##(mówimy o tym "w sygnaturze funkcji"),
##to polecenie importujące moduł datetime trzeba
##przesunąć z definicji funkcji (ciała funkcji) na początek skryptu.
##Pozwoli to na korzystanie z funkcji date.today() 

#1
def PrintAnimal(animal=""):
        # this function prints ascii-art
    cat = r'''
    |\---/|
    | o_o |
     \_^_/'''

     
    bear = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''


    bat = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
    if animal == "cat":
        print(cat)
    elif animal == "bear":
        print(bear)     
    elif animal == "bat":
        print(bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" %animal)
    return

PrintAnimal()
PrintAnimal("cat")
PrintAnimal("bear")
PrintAnimal("bat")
PrintAnimal("rat")
PrintAnimal(animal='bat')

#2
from datetime import date

def DaysToEndOfYear(year=date.today().year, \
                    month=date.today().month, \
                    day=date.today().day):

    date_today = date(year, month, day)
    print (date_today)
    date_end_year = date(year, 12, 31)
    print (date_end_year)
    delta = date_end_year - date_today
    print(delta.days)
    return
DaysToEndOfYear()
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)

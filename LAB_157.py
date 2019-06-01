##Sekcja 9, wykład 157
##ZADANIE 1
##Nadal poprawiamy znane Ci funkcje. Zaczynamy od PrintAnimal.
##Zmień definicję funkcji tak, aby można było przekazać
##zmienną ilość nazw zwierząt, które mają być narysowane.
##Na tym etapie rezygnujemy ze zwracania wartości oraz wartości domyślnej.
##Po zmianach przetestuj działanie funkcji przekazując
##po kilka nazw zwierząt jako parametr
##(wybieraj spośród tych zdefiniowanych w funkcji, jak i niepoprawnych)
##
##ZADANIE 2
##A teraz kolej na DaysToEndOfYear:
##    zmień parametr tak, aby przyjmował wiele dat
##    (uwaga funkcja będzie przyjmować daty,
##     a nie osobne wartości rok/miesiąc/dzień)
##    dla każdej daty z parametrów ma zostać wyświetlona informacja
##    o dacie i ilości dni do Sylwestra
##    usuń część funkcji odpowiadającą za zwracanie wartości
##    przetestuj działanie funkcji przekazując różną ilość argumentów

#1
def PrintAnimal(*animals):
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
    for animal in animals:
        if animal == "cat":
            print(cat)
        elif animal == "bear":
            print(bear)
        elif animal == "bat":
            print(bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" %animal)
    return 


##PrintAnimal()
PrintAnimal("cat","bear","rat")
##PrintAnimal("bear")
##PrintAnimal("bat")
##PrintAnimal("rat")
##PrintAnimal(animal='bat')

#2


from datetime import date
 
def DaysToEndOfYear(*dates):
 
    for date_today in dates:
        
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
 
DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())

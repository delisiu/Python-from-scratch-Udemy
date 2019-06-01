##Sekcja 9, wykład 154
##ZADANIE 1
##Nadal pracujemy nad tymi samymi funkcjami, co poprzednio.
##Zaczynamy od funkcji PrintAnimal.
##Należy zwrócić informację o tym czy obrazek został wyświetlony, czy nie:
##    Jeżeli przekazano poprawny parametr i obrazek został wyświetlony,
##    należy zrócić wartość True
##    Jeżeli przekazano niepoprawny parametr i obrazek nie został wyświetlony,
##    należy zwrócić False
##Przetestuj działanie funkcji po zmianie
##
##ZADANIE 2
##Teraz modyfikujemy funkcję DaysToEndOfYear.
##Ilość dni do Sylwestra nie ma być wyświetlana,
##ale zamiast tego zwracana.
##Przetestuj działanie funkcji

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
        return False 
    return True


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
##    print (date_today)
    date_end_year = date(year, 12, 31)
##    print (date_end_year)
    delta = date_end_year - date_today
##    print(delta.days)
    return delta.days
DaysToEndOfYear()
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)

print('Date: 2020-12-20 days to end of year: %d' %( DaysToEndOfYear(2020,12,20)))
 
print('Date: 2020-12-21 days to end of year: %d' %( DaysToEndOfYear(2020,12,21)))
 
print('Date: TODAY days to end of year: %d' %( DaysToEndOfYear()))

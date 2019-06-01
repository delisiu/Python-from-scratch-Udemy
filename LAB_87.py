##Sekcja 7, wykład 87
##
##1. Pamiętasz zadanie "za karę" dodające kolejne liczby?
##Oto propozycja rozwiązania. Skopiuj ją do własnego skryptu i uruchom:
##
##    number = 1
##    previus_number = 0
##     
##    while number<50:
##        print(number + previus_number)
##        previus_number=number
##        number+1
##
##opsss.... zawiesiło się? Skrypt można przerwać naciskając CTRL+C.
##Korzystając z debuggera znajdź błąd
##(znajdź go nawet jeśli już widzisz co jest nie tak ;))
##W odpowiedziach znajdziesz opis przyczyny problemu
##
##2. Poniższy program ma za zadanie (w nieco dziwny sposób!)
##utworzyć napis o długości 10 znaków zapisany w zmiennej text.
##Niestety coś poszło nie tak. Korzystając z debuggera znajdź przyczynę.
##W odpowiedziach znajdziesz poprawną wersję skryptu z komentarzem
##
##    text = ''
##    number = 10
##    condition = True
##     
##    while condition:
##     
##        text+='x'
##        print(text)
##        
##    if len(text)>number:
##        condition=False

#1
##number = 1
##previus_number = 0
##     
##while number<50:
##    print(number + previus_number)
##    previus_number=number
##    number+=1
#2
text = ''
number = 10
condition = True
     
while condition:
     
    text+='x'
    print(text)
        
    if len(text)>number:
        condition=False

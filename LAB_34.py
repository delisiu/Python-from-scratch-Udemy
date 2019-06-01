##Sekcja 4, wykład 34
##
##1 Utwórz zmienną quote i przypisz jej następującą wartość:
##'A good programmer is someone who always looks both ways before crossing a one-way street'
##2 Wyświetl tekst napisany tylko wielkimi literami
##3 Wyświetl tekst zapisany tylko małymi literami
##4 Sprawdź czy tekst kończy się słowem 'street'
##5 Sprawdź czy tekst jest zapisany wielkimi literami
##6 Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
##7 Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
##8 Zamień w tekście słowo 'one' na '1'
##9 Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2
##10 Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
##11 Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
##
##W ostatnim zadaniu otrzymujesz 4 wartości false.
##Zwłaszcza 2 ostatnie wyniki mogą Cię dziwić.
##Nasz napis zawierał spacje, składał się z wielu wyrazów
##i dlatego nie jest alfa-stringiem ani alfanumerykiem
#1
quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
#2
print(quote.upper())
#3
print(quote.lower())
#4
print(quote.endswith('street'))
#5
print(quote.isupper())
#6
print(quote.upper().isupper())
#7
print(quote.find("one"))
#8
print(quote.replace("one","1"))
#9
print(quote.replace('one','1').replace('both','2'))
#10
print(quote.split(" "))
#11
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())

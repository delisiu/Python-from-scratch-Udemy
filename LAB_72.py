##Sekcja 6, wykład 72
##
##Kontynuujemy przykłady z poprzedniej lekcji
##1.
##Jak pamiętasz (mam nadzieję) sklep odzieżowy uruchamiał promocję
##tylko jeżeli ilość lajków była większa lub równa 500
##a ilość udostępnień co najmniej 100.
##Kiedy oba warunki były spełnione sprawa była prosta -
##rozpoczynała się obniżka cen.
##Kiedy jednak brakowało lajków lub udostępnień,
##to wypadałoby dać znać czego brak.
##Najpierw napisz zagnieżdżone wyrażenie if / else,
##a potem przekształć do postaci if/elif/else.
##Możesz to zrobić "po swojemu",
##ale jak chcesz możesz stosować się do moich podpowiedzi.
##To propozycje kroków w rozwiązaniu z zagnieżdżonymi if/else
##jeśli warunki są spełnione - świetnie, rozpoczynamy promocj
##w przeciwnym razie
##jeśli brakuje lajków wyświetl informację o braku lakjów
##w przeciwnym razie (musi brakować udostępnień - to logiczne!)
##wyświetl informację o braku udostępnień
##Przepisujac instrukcje do if/elif/else stosuj sie do tych zaleceń:
##jeśli warunki są spełnione, zaczynamy promocję
##w przeciwnym razie jeśli ilość lajków jest za mała
##- wyświetl komunikat o brakujących lajkach
##w przeciwnym razie wyświetl komunikat o brakujących udostępnieniach
##2.
##Restauracja oferowała kupon na burgera,
##jeżeli zamówiłeś pizzę lub duży napój w dzień nie będący dniem weekendowym.
##Kiedy warunki promocji były spełnione, sprawa była prosta - dajemy kupon.
##Jednak w przypadku niespełnienia warunków wypadałoby poinformować,
##który warunek nie jest spełniony.
##Wskazówki do rozwiązania z zagnieżdżonym if/else
##jeżeli warunki są spełnione wydajemy kupon na burgera
##w przeciwnym razie
##jeżeli jest weekend, to wyświetlamy informację,
##że promocja dotyczy tylko dni poza weekendem
##w przeciwnym razie (już wiadomo, że to nie jest weekend,
##więc brakło na zamówieniu pizzy lub dużego napoju!)
##wyświetlamy informację o braku pizzy 
##Przepisując rozwiązanie na if/elif/else stosuj się do wskazówek:
##jeśli warunki są spełnione - wydaj kupon na burgera
##w przeciwnym razie jeśli jest to weekend, wyświetl komunikat o tym,
##że promocja obowiązuje wyłącznie w poza weekendem
##w przeciwnym razie wyświetl komunikat o tym,
##że należy zamówić pizze lub duży napój
##Pamiętaj, że stosowanie if/elif/else jest znacznie lepsze
##jeśli chodzi o styl programowania!
#1
numLikes=400
numShares=155

minLikes=500
minShares=100
if minLikes<=numLikes and minShares<=numShares:
    print("Discount!!! 10%!!!")
elif numLikes<minLikes:
    print("Too small numer of likes to discount")
else:
    print("Too small numer of shares to discount")
#2
isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False
if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Masz kupon na burgera")
elif isWeekend:
    print("Come to us on week to get Free Burger!")
else:
    print("Consider buying Pizza or BigDrink to have Burger for free")

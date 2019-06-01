##Sekcja 6, wykład 69
##
##1.  (*) - proszę wybacz niepoprawną pisownię lajk i share ;)
##Pracujesz dla firmy odzieżowej, której celem jest
##wypromowanie nowej kolekcji ubrań.
##Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień"
##na Facebooku. Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków"
##i co najmniej 100 "udostępnień", to ceny spadną o 10%.
##Na razie masz napisać fragment programu,
##który rozstrzygnie czy warunki promocji są spełnione czy nie.
##Jeśli już wiesz jak to zrobić "GO ON!",
##a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:
##zadeklaruj zmienną MIN_LIKES  o wartości 500 i MIN_SHARES o wartości 100
##zadeklaruj zmienną num_likes i num_shares
##o wartościach wskazujących na to ile było kliknięć LIKE i SHARE na Facebooku.
##Przypisz tym zmiennym wybrane przez CIebie wartości.
##Zmieniając te wartości będziesz testować poprawność swojego programu,
##np 1300 lajków i 55 sharów
##napisz polecenie IF, które w przypadku spełnienia warunku opisanego na początku,
##wyświetli komunikat o obniżce ceny, a w przeciwnym razie wyświetli
##komunikat o braku wystarczającej ilości lajków i sharów
##przetestuj działanie polecenia IF zmieniając wartości zmiennych
##num_like i num_shares
##2.
##Pracujesz dla restauracji, która chce nagrodzić klientów
##zamawiających w dni robocze (poza weekendem) pizze lub duży napój.
##Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
##Na razie piszesz polecenie decydujące o spełnieniu warunków promocji.
##Do dyspozycji masz zmienne:
##isPizzaOrdered - o wartości True/False,
##która informuje, czy klient kupił Pizzę
##isBigDrinkOrdered - o wartości True/False,
##która informuje, czy klient zamówił duży napój
##isWeekend - o wartości True/False,
##która informuje, czy jest weekend
##Napisz polecenie IF, które w przypadku,
##gdy klient kupił pizzę lub duży napój w dzień poza weekendem,
##wyświetli informację o kuponie na Burgera,
##a w przeciwnym razie wyświetli komunikat zachęcający do dalszych zakupów.
##Zmieniaj wejściowe warunki logiczne i testuj,
##czy polecenie zwraca oczekiwany napis.
##3.
##Twój zespół opracowuje przeglądarkę internetową w Pythonie!
##Twoim zadaniem jest sprawdzenie, czy operacja pobierania pliku
##na dysk ma się szansę udać, czy jest od razy skazana na porażkę
##ze względu na brak miejsca na dysku.
##Na wejściu masz następujące zmienne:
##diskSize - zmienna numeryczna (np. o wartości 140)
##oznaczająca wielkość dysku w GB
##diskSizeUsed - zmienna numeryczna (np. o wartości 133)
##oznaczająca ilosć zajętego miejsca na dysku w GB
##fileSize - zmienna numeryczna (np o wartości 10)
##oznaczająca wielkość pobieranego pliku w GB
##Zbuduj polecenie IF, które w przypadku,
##gdy jest wystarczająco wolnego miejsca na dysku wyświetli komunikat
##"File can be downloaded".
##W przypadku, gdy plik jest za duży,
##ma być wyświetlony komunikat o braku miejsca na dysku
##Zmieniając parametry wejściowe przetestuj działanie polecenia
#1
numLikes=100
numShares=155

minLikes=500
minShares=100
if minLikes<=numLikes and minShares<=numShares:
    print("Discount!!! 10%!!!")
else:
    print("Too small numer of likes and shares to discount")
#2
isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True
if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Masz kupon na burgera")
else:
    print("Come to us on weekend and consider buying Pizza or BigDrink to have Burger for free")
#3
diskSize = 140
diskSizeUsed = 130
fileSize = 10
if diskSize-diskSizeUsed>=fileSize:
    print('File can be downloaded')
else:
    print('No space on disc to download file')

##Sekcja 5, wykład 66
##
##Nadal analizujesz wydajność kanałów, jakimi można dotrzeć do klientów.
##Każdorazowo po zmienie słownika wyświetl jego zawartość
##1. Utwórz obiekt dictionary o nazwie chanels z następującymi kluczami i wartościami:
##-Google - 1480
##-Email - 300
##-Natural Traffic - 440
##-TV Spot - 700
##2. Wyświetl wartość skojarzoną z kluczem "Email"
##3. Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:
##-Natural Traffic -  520
##-News - 600
##4.Zaktualizuj słownik chanels wartościami z chanelsUpdate
##5. Wyświetl wszystkie klucze z chanels
##6. Usuń wartość 'Email' ze słownika
#1
chanels={"Google":1480,"Email":300, "Natural Traffic":440, "TV Spot":700}
print(type(chanels))
print(chanels)
#2
print(chanels['Email'])
#3
chanelsUpdate={'Natural Traffic':520,'News':600}
print(chanels)
print(chanelsUpdate)
#4
chanels.update(chanelsUpdate)
print(chanels)
print(chanelsUpdate)
#5
print(chanels.keys())
print(chanels.items())
print(chanels.values())
#6
print(chanels)
chanels.pop('Email')
print(chanels)
chanels.popitem('Email',300)
print(chanels)

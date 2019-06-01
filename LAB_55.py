##Sekcja 4, wykład 55
##
##1.  Anagram to słowa, które składają sie z tych samych liter,
##ale mające różne znaczenia np. "arbuz" >> "burza", "alergia" >> "galeria".
##Tu pobawimy się trochę anagramami.
##2. Tutaj każdą literkę wyodrębnisz i wykorzystasz oddzielnie.
##Do zmiennej q zapisz tekst "THE EYES".
##Wyświetl napis zbudowany z liter zmiennej q w kolejności: 0,1,2,5,3,7,4,6.
##Wyświetlając literki skorzystaj z print
##lub dodaj do siebie literki budując napis.
##3. Tutaj użyjesz notacji, która pozwoli wyodrębnić fragment napisu
##rozpoczynając od określonej pozycji do końca.
##Do zmiennej q zapisz  "a gentleman"
##a potem wyświetl litery w kolejności 3,6,7,2,0,4,5,1,8 - do końca
##4. Wiesz jak z napisu  "THE MORSE CODE" zrobić tekst "HERE COME DOTS"?
##Gdzie się da korzystaj z notacji "od-do"
##5. Zostajesz zatrudniony w firmie,
##która wykonuje analizę oglądalności poszczególnych programów TV.
##Na bardzo początkowym etapie, Twój program musi przeczytać dane z pliku
##tekstowego z zapisanym harmonogramem poszczególnych programów.
##Plik zawiera linie zbudowane tak,
##że tytuł programu znajduje się w cudzysłowiu,
##a kończy się napisem o:, po którym następuje godzina, np tak:
##'Program "Kropka nad i" nadamy o: 22:00'
##Musisz wyodrębić tytuł programu i godzinę o której zostanie nadany.
##W tym celu:
##Do zmienej line wpisz tekst "'Program "Kropka nad i" nadamy o: 22:00'"
##Do zmiennej time wyodrębnij samą tylko godzinę
##(musisz poszukać znaku dwukropek i pobrać wszystkie dalsze znaki)
##Wyświetl napis time
##Do zmiennej tmp wyodrębnij fragment tekstu ze zmiennej line
##rozpoczynający się za znakiem cudzysłów do końca
##Do zmiennej title wyodrębnij z tmp fragment tekstu
##od początku do znaku cudzysłów
##Wyświetl title i time
#2
q="THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])
#3
q="a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8]+q[9:])
#4
q="THE MORSE CODE"
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])
print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])
#5
line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[ line.find(':')+2 : ]
print(time)
tmp=line[ line.find('"')+1 : ]
print(tmp)
title=tmp[:tmp.find('"')]
print(title, time)

##Sekcja 4, wykład 46
##
##1. Zadeklaruj zmienną name i przypisz do niej swoje imie
##2. Zadeklaruj zmienną age i przypisz do niej wiek
##3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365
##4. Zadekraruj zmienną message i przypisz jej wartość jak poniżej.
##Uwaga w miejscu ??? należy umieścić znaczniki
##pozwalające na wyświetlenie kolejno napisu i dwóch liczb
##'??? is ??? years old, so is about ??? days old' 
##5. Wyświetl informację jak poniżej
##(wykorzystaj funkcje formatowania napisów)j:
##Jan is 26 years old, so is about 9490 days old 
##6. Zmień imie i wiek w zmiennych name i age i jeszcze raz
##wyświetl komunikat korzystając z tej samej instrukcj co poprzednio
##7. Zmień wartość zmiennej message na:
##message = '{???} is {???} years old, so is about {???} days old' 
##Ponownie w miejscu ??? należy umieścić odpowiednie napisy
##formatujące pozwalające wyświetlić napis i 2 liczby
##8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:
##Chris is 17 years old, so is about 6205 days old 
##9. Wyznacz wynik dzielenia całkowitego i resztę
##z dzielenia 1234567890 przez 12345:
##Wynik powinien wyglądać tak:
##1234567890 divided by 12345 is  100005 and the rest is 6165
#1-5
name="Maciek"
age=36
daysInYear=365
massage="%s is %d years old, so is about %d days old"
print(massage%(name,age,daysInYear*age))
#6
name="Ewa"
age=5.5
print(massage%(name,age,daysInYear*age))
#7-8
name="Chris"
age=17
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,daysInYear*age))
#9
print('1234567890 divided by 12345 is ',1234567890 // 12345,
      'and the rest is',1234567890 % 12345)
print('4 divided by 3 is ',4 // 3,
      'and the rest is',4 % 3)

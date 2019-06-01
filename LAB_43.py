##Sekcja 4, wykład 43
##1. Zadeklaruj zmienną helloMessage i wpisz do niej tekst:
##"Hello %s!"
##2. Korzystając z tej zmiennej oraz z operatora % wyświetl
##dwa powitania: raz %s należy zamienić na Kate a raz na Chirs
##3. Zmień zawartość zmiennej helloMessage na
##"Hello {0:s}!"
##4. Podobnie , jak w punkcie drugim wyświetl powitanie z Kate i Chis,
##ale tym razem skorzystaj z metody format
##5. Zmień zawartość zmiennej helloMessage na
##"%s has %d %s"
##6. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa komunikaty.
##    w pierwszym komunikacie %s zamień na Kate, %d na 1, a %s na animal
##    w drugim komunikacie %s zamień na  Chris, %d na 100000, a %s na $
##7. Zmień zawartość zmiennej helloMessage na
##"{0:s} has {1:d} {2:s}"
##8. Wyświetl te same komunikaty, jak w punkcie 6,
##ale tym razem skorzystaj z metody format
##9. [Trochę trudniejsze, ale cała trudność polega na samodzielnym
##    zbudowaniu napisu formatującego i to w takiej postaci,
##    że na każdy element w napisie ma zostać przewidziana
##    określona liczba znaków]
##Utwórz zmienną line i wpisz do niej tekst pozwalający na
##wyświetlenie na 20 znakach pewnego napisu,
##następnie słowa "costs", następnie na 6 znakach pewnej
##liczby i następnie znaku €, np:
##    ICE CREAM            costs      3 €
##    TRIP TO VENICE       costs    119 €
##    PIZZA HAWAII         costs      6 €
##... BTW, wiesz jak uzyskać znak € z klawiatury?
##O ile używasz Windows powinien zadziałać prawy ALT + u
##10. Korzystając ze zmiennej line i polecenia print,
##zamieniaj odpowiednie znaczniki na podane niżej wartości,
##tak aby w efekcie został wyświetlony cennik usług:
##    ICE CREAM    3
##    TRIP TO VENICE  119
##    PIZZA HAWAI  6 
#1
helloMessage="Hello %s!"
#2
print(helloMessage%("Kate"))
print(helloMessage%("Chris"))
#3
helloMessage="Hello {0:s}!"
#4
print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))
#5
helloMessage="%s has %d %s"
#6
print(helloMessage%("Kate",1,"animal"))
print(helloMessage%("Chris",100000,"$"))
#7
helloMessage="{0:s} has {1:d} {2:s}"
#8
print(helloMessage.format("Kate",1,"animal"))
print(helloMessage.format("Chris",100000,"$"))
#9
line = "{0:20s} costs {1:6d} €"
 
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))
#10
line = "{0:2}{1:20s} {2:6d} "
 
print(line.format('\a','ICE CREAM',3))
print(line.format('\a','TRIP TO VENICE',119))
print(line.format('\a','PIZZA HAWAII',6))
#10B
line = "\a {0:20s} {1:6d} "
 
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))

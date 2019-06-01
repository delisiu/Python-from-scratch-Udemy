##Sekcja 7, wykład 104
##
##ZADANIE 1
##Na konto została wpłacona kwota initialCapital w wysokości 20000.
##Oprocentowanie na koncie to percent = 0.03.
##Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat.
##Po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności
##i zarabia odsetki przez pozostały czas.
##Zadeklaruj wymagane zmienne, a następnie stwórz pętlę,
##która wyświetli informację o tym ile pieniędzy jest na koncie pod koniec roku,
##kiedy odsetki się kapitalizują.
##Dodaj na zakończenie informację o całkowitej kwocie zarobionej w banku.
##
##ZADANIE 2
##Dana jest liczba całkowita dodatnia number = 20730906,
##Oblicz sumę cyfr tej liczby.
##Wskazówka 1:
##-utwórz pomocniczą zmienną, która będzie podlegała modyfikacji
##podczas pracy programu
##-warunkiem pętli może być sprawdzanie, czy ta pomocnicza zmienna jest >0
##-aby wyliczyć ostatnią cyfrę podziel pomocniczą zmienną modulo (operator %) 10
##-aby usunąć ostatnią cyfrę z pomocniczej zmiennej podziel ją cąłkowiicie
##( operator // )  przez 10 i wynik zapisz w tej samej pomocniczej zmiennej
##
##Wskazówka 2:
##Skorzystaj z tego opisu, jeżeli nadal nie masz pomysłu na rozwiązanie.
##Ten opis, to jakby słowne opowiedzenie tego co robi program:
##Mamy liczbę 20730906 zapisną, a jakże inaczej w systemie DZIESIĘTNYM.
##Kiedy tą liczbę podzielę modulo (symbol działania %) przez 10 (dzielenie modulo zwraca resztę z dzielenia) to dostaniemy 6 - czyli ostatnią cyfrę.
##Potem ta ostatnia cyfra już mnie nie obchodzi. Więc dzielę bez reszty (symbol działania //) przez 10. W wyniku dostaję więc liczbę 2073090.
##I od początku:
##Mamy liczbę 2073090 i dzielę ją modulo % przez 10. Zwrócona reszta to 0
##Teraz ostatnia cyfra już mnie nie obchodzi, więc dzielę bez reszty // przez 10. W wyniku dostaję liczbę 207309.
##I od początku:
##Mamy liczbę 207309 i dzielę ją modulo % przez 10. Zwrócona reszta to 9
##Teraz ostatnia cyfra już mnie nie obchodzi, więc dzielę bez reszty // przez 10. W wyniku dostaję liczbę 207309
##i tak dalej, aż dojdę do zera.
##
##ZADANIE 3
##Dany jest tekst:
##United Space Alliance: This company provides major support to NASA for
##various projects, such as the space shuttle. One of its projects is to
##create Workflow Automation System (WAS), an application designed to
##manage NASA and other third-party projects. The setup uses a central
##Oracle database as a repository for information. Python was chosen over
##languages such as Java and C++ because it provides dynamic typing and
##pseudo-code–like syntax and it has an interpreter. The result is that
##the application is developed faster, and unit testing each piece is easier.
##policz ile jest w nim słów dłuższych od wordLength = 6
##Wskazówka:
##-jako słowo potraktujemy każdy ciąg znaków rozdzielony spacją
##-aby tekst podzielić na słowa skorzystaj z funkcji split(' ')
##i zapisz wynik w liście listOfWords
##-zadeklaruj zmienne shortWords i longWords=0
##-pętlą przejdź przez listę słów i poleceniem IF badaj
##czy napis jest służszy od wordLength.
##Jeśli tak zwiększ liczbę longWords o 1, a jeśli nie to zwiększ shortWords

#1
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
i=1
nowCapital=initialCapital
while i <= maxTimeYears:
    print("Oszczędnosci na koniec",i,"wynoszą",nowCapital+nowCapital*percent)
    i+=1
    nowCapital=nowCapital+nowCapital*percent
print('-------------------------------------------------------')
#2
number = 20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits,)
print('-------------------------------------------------------')
#3
text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
wordLength = 6
words=text.replace('\n',' ').split(" ")
i=0
result=0
while i<len(words):
    if len(words[i])>wordLength:
        result+=1
    i+=1
print (result)

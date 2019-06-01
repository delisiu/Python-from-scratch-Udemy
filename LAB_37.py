##Sekcja 4, wykład 40
##
##Czy wiesz, że twórca języka Python - Guido Van Rossum
##- był fanem latającego cyrku Monty Pythona?
##Tak. To od tego wzięła się nazwa języka!
##
##1. Wejdź na stronę Wikipedii poświęconej Monty Pytonowi.
##Skopiuj fragment z paragrafu zatytuowanego "Latający cyrk Monty Pythona".
##2. W skrypcie utwórz zmienną article i przypisz jej wartość skopiowanego tesktu.
##Uwaga! Skopiowany tekst jest długi i zawiera znaki ENTER.
##Jeśli chcesz przypisać do zmiennej taki tekst możesz użyć konstrukcji z trzema apostrofami o tak:
##zmienna = '''
##dłuuugi tekst i jeszcze 
##dłuższy tekst i....
##'''
##3. Skonwertuj tekst do dużych liter i wyświetl go.
##Zrób to w jednej instrukcji.
##
##4. Wyświetl tekst zamieniając 'monty' na 'flying'.
##Ponieważ python rozpoznaje małe i duże litery przed zamianą
##skonwertuj go na małe litery.
##Ponownie postaraj się to zrobić w jednym poleceniu.
##5. Rozbij tekst na słowa ze względu na spacje i wyświetl tą listę.
##6. Wyświetl tekst w postaci:
##        word python appears 3 times 
##oczywiście liczba (tutaj 3) powinna być wyliczona,
##jako ilość wystąpień tekstu python w zmiennej article
##7. Poleceniem print wyświetl tekst:
##to print the \ you need to put \ twice in your text like this: \\ 
##8. Poleceniem print wyświetl tekst
##The best hits of '80s!!! 
##Zrób to na 2 sposoby:
##-raz tekst powinien być zamknięty w pojedynczym apostrofie '
##-a drugi raz tekst powinien być zamknięty w cudzysłowiu "
##9. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut.
##Chcemy wyświetlić tabelkę w postaci:
##
##    cur   exchange amount
##    USD   3.65     64.10958904109589
##    EUR   4.23     55.31914893617021
##w tym celu:
##-najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234
##-następnie wyświetl teksty rozdzielając wartości tabulatorem,
##tak aby to co zostanie wypisane na ekranie przypominało tabelkę
##(skorzystaj do tego z kilku poleceń print,
## jednolinijkowy print byłby zbyt trudny do zrozumienia)
##-wartości w kolumnie amount wylicz dzieląc amountPLN przez aktualny kurs USD
##i EUR (w tym przykładzie są to 3.65 i 4.23)
##10. Zadeklaruj zmienną ValueAsText i wpisz do niej wartość '123.45'
##11. Zadeklaruj zmienną factor o wartości 1.23
##12. Wyświetl tekst:
##value is  123.45 factor is 1.23 value*factor= 151.8435 
##podczas obliczania value * factor skonwertuj zmienną ValueAsText na typ float
##
##
#1#2
article='''
Pierwsza seria „Latającego cyrku” miała pierwotnie dawać główne pole do popisu Cleese’owi, ten chciał jednak współpracować z innymi. Tak oto powstała zorganizowana grupa, dla której utworzono rutynowe zasady działania. Każdy dzień pisania rozpoczynał się o 9:00 rano i trwał do 17:00. Na początku typowego tygodnia pracy Cleese i Chapman pisali w odosobnieniu jako jedna spółka autorska, Jones i Palin jako druga, a Idle pisał sam. Po kilku dniach cała grupa spotykała się wraz z Gilliamem i krytykowała nawzajem swoje scenariusze oraz wymieniała poglądy. Podchodzili do pisania demokratycznie. Jeśli coś rozśmieszyło większość, zatwierdzano to jako część programu. W podobny sposób obsadzano role – nie było problemów z egocentryzmem, gdyż każdy z Pythonów czuł się bardziej autorem niż aktorem. Po dobraniu i uporządkowaniu kolejności skeczy do danego odcinka, Gilliam miał wolną rękę w łączeniu ich w całość za pomocą wymyślnych animacji, uzbrojony w kamerę, nożyczki i farbę.

Zanim wymyślono nazwę „Latający cyrk Monty Pythona”, powstało kilka innych tytułów roboczych, m.in. Owl Stretching Time (Pora rozciągania sów), Bunn, Wacket, Buzzard, Stubble and Boot, Gwen Dibley's Flying Circus (Latający Cyrk Gwen Dibley).

Zespół miał bardzo konkretny pomysł na serial i był bardzo zawiedziony, gdy Spike Milligan nagrał swój program komediowy Q5 w nieco podobnym duchu. Pythoni przyznawali się do inspiracji Milliganem, lecz styl „Latającego cyrku” jest zdecydowanie inny. Wyróżniają go szczególnie niepowtarzalne animacje Gilliama, ale także proces wzajemnej krytyki i selekcji materiału.
'''
#3
print(article.upper())
#4
print(article.lower().replace("monty","flying"))
#5
print(article.split(" "))
#6
print("word python appears", article.lower().count("python"), "times")
#7
print("to print the \ you need to put \ twice in your text like this: \\\ ")
#8
print("The best hits of '80s!!! ")
print('The best hits of \'80s!!! ')
#9
amountPLN = 234
USD =3.65
EUR= 4.23
amount = amountPLN / USD
print('cur','\texchange','amount')
print('USD',"\t",USD,"\t",int(amountPLN/USD))
print('EUR','\t',EUR,"\t",amountPLN/EUR)
ValueAsText ='123.45'
factor = 1.23
print ("value is", ValueAsText, "factor is ",
       factor, "value*factor=", float(ValueAsText)*factor)


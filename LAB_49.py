##Sekcja 4, wykład 49
##
##Zostajesz zatrudniony(a) do stworzenia oprogramowania pokładowego
##nowoczesnego samochodu.
##Aktualnie Twoim zadaniem jest oprogramowanie sterownika
##odpowiedzialnego za automatyczne włączanie świateł mijania w samochodzie.
##Będziesz pracować z następującymi zmiennymi:
##
##isAutomaticMode - zmienna logiczna, o następującym znaczeniu:
##wartość True oznacza, że kierowca ustawił pokrętło sterujące światłem
##na tryb automatyczny.
##Sterownik ma podejmować decyzję o zapaleniu świateł
##tylko jeżeli wartość tej zmiennej to True,
##ale zapalenie świateł zależy jeszcze od kolejnych warunków,
##
##is80PercentLight - zmienna logiczna o następującym znaczeniu:
##wartość True oznacza, że "chyba" mamy dzień, bo jest dość dużo światła.
##Światła w samochodzie powinny być zgaszone o ile nie ma innych warunków,
##które wpływałyby na to, że światła mają się świecić.
##Jeśli wartość zmiennej to False, tzn. że jest dość ciemno
##i światła powinny się zaświecić,
##oczywiście o ile jesteśmy w trybie automatycznym
##
##isDirectLight - zmienna logiczna o następującym znaczeniu:
##wartość True oznacza, że nisko położone słońce świeci wprost w oczy kierowcy.
##Wprawdzie ciemno nie jest, ale w takich warunkach światła powinny się zaświecić,
##oczywiście jeśli jesteśmy w trybie automatycznym
##
##isRainy - zmienna logiczna o następującym znaczeniu:
##wartość True oznacza, że pada deszcz,
##jest mgła lub mamy do czynienia z innymi niekorzystnymi warunkami atmosferycznymi.
##O ile jesteśmy w trybie automatycznym, to należy zaświecić światła
##
##Do zmiennej turnLightsOn zapisz wynik wyrażenia, które w oparciu o w/w zmienne ustali, czy światła mają zostać zapalone czy nie. Potem wyświetl wynik korzystając z instrukcji:
##
##    print("Automatic mode:   ",isAutomaticMode)
##    print("Is the light good:",is80PercentLight)
##    print("Is sun low:       ",isDirectLight)
##    print("Is it rainy:      ",isRainy)
##    print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode=True
is80PercentLight=True
isDirectLight=True
isRainy=True
turnLightsOn=isAutomaticMode and(not is80PercentLight or isDirectLight or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn=isAutomaticMode and(not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

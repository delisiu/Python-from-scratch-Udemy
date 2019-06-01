##Sekcja 7, wykład 102
##
##Twoim zadaniem jest stworzenie fragmentu programu,
##który wyświetla menu z opcjami do wyboru,
##a następnie zależnie od dokonanego wyboru wykona pewne czynności.
##Zadeklaruj zmienne:
##
##    menu = '''
##    Choose what you want me to do for you:
##    1 - COFFEE
##    2 - TEA
##    3 - MAKE ME SMILE
##    ---------------
##    To stop this script select 0
##    '''
##     
##    smile = '''
##     
##                              oooo$$$$$$$$$$$$oooo
##                          oo$$$$$$$$$$$$$$$$$$$$$$$$o
##                       oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
##       o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
##    oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
##    "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
##      $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
##      $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
##       "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
##        $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
##       o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
##       $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
##      o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
##      $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
##     """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
##                "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
##                  $$$o          "$$""$$$$$$""""           o$$$
##                   $$$$o                                o$$$"
##                    "$$$$o      o$$$$$$o"$$$$o        o$$$$
##                      "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
##                         ""$$$$$oooo  "$$$o$$$$$$$$$"""
##                            ""$$$$$$$oo $$$$$$$$$$
##                                    """"$$$$$$$$$$$
##                                        $$$$$$$$$$$$
##                                         $$$$$$$$$$"
##                                          "$$$""""
##    '''
##
##Napisz pętlę while, która będzie działać w nieskończoność.
##W tej pętli:
##wyświetl napis menu z dostępnymi opcjami
##wczytaj do zmiennej letter wybór użytkownika
##napisz polecenie if, które w przypadku, gdy w letter znajduje się 1
##wyświetli informację "Function COFFEE not implemented"
##poprosi o naciśnięcie ENTER
##wróci na początek pętli while
##napisz polecenie  if, które w przypadku, gdy w letter znajduje się 2
##wyświetli informację "Function TEA not implemented"
##poprosi o naciśnięcie ENTER
##wróci na początek pętli while
##napisz polecenie if, które w przypadku, gdy w letter znajduje się 3
##wyświetli napis znajdujący się w zmiennej smile
##poprosi o naciśnięcie ENTER
##wróci na początek pętli while
##napisz polecenie if, które w przypadku, gdy w letter znajduje sie 0
##przerwie działanie nieskończonej pętli while
##w każdym pozostałym przypadku wyświetli instrukcję
##czekając na naciśnięcie ENTER:
##"You need to make a valid choice. Press ENTER and try again!"
menu = '''
    Choose what you want me to do for you:
    1 - COFFEE
    2 - TEA
    3 - MAKE ME SMILE
    ---------------
    To stop this script select 0
    '''
     
smile = '''
     
                              oooo$$$$$$$$$$$$oooo
                          oo$$$$$$$$$$$$$$$$$$$$$$$$o
                       oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
       o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
    oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
    "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
      $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
       "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
        $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
       o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
       $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
      o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
      $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
     """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
                "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
                  $$$o          "$$""$$$$$$""""           o$$$
                   $$$$o                                o$$$"
                    "$$$$o      o$$$$$$o"$$$$o        o$$$$
                      "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                         ""$$$$$oooo  "$$$o$$$$$$$$$"""
                            ""$$$$$$$oo $$$$$$$$$$
                                    """"$$$$$$$$$$$
                                        $$$$$$$$$$$$
                                         $$$$$$$$$$"
                                          "$$$""""
    '''
while True:
 
    print(menu)
    letter = input('Enter your choice  ')
 
    if letter == '1':
        print("Function COFFEE not implemented")
        input('Press enter')
        continue
    
    if letter == '2':
        print("Function TEA not implemented")
        input('Press enter')
        continue
    
    if letter =='3':
        print(smile)
        input('Press enter')        
        continue
        
    if letter == '0':
        break
 
    input('You need to make a valid choice. Press ENTER and try again!')

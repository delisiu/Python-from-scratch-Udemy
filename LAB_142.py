##Sekcja 9, wykład 142
##Przygotowujesz sktypty, które nie tylko wykonają pewne czynności,
##ale dodatkowo wygenerują raport,
##który będzie oznaczony logo firmy.
##Naszym logo będzie kot, miś lub nietoperz.
##Napisz funkcje:
##    PrintCat() - wyświetlającą kota
##    PrintBear() - wyświetlającą misia
##    PrintBat() - wyświetlającą nietoperza.
##Oto dane, które przydadzą się w tym zadaniu:
##
##        txt = r'''
##    |\---/|
##    | o_o |
##     \_^_/'''
##        txt = r'''
##    /  \.-"""-./  \
##    \    -   -    /
##     |   o   o   |
##     \  .-'"'-.  /
##      '-\__Y__/-'
##         `---`'''
##        txt = r'''
##       /\                 /\
##      / \'._   (\_/)   _.'/ \
##     /_.''._'--('.')--'_.''._\
##     | \_ / `;=/ " \=;` \ _/ |
##      \/ `\__|`\___/`|__/`  \/
##              \(/|\)/       '''
##(więcej fajnych obrazków znajdzisz np tu: https://www.asciiart.eu/

def PrintCat():
    #rysuje kota

    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print (txt)
    return

def PrintBear():
    #rysuje misia
            
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print (txt)
    return

def PrintBat():
    #rysuje nietoperza
    txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''

    print (txt)
    return

PrintCat()
PrintCat()
PrintCat()
PrintBear()
PrintBear()
PrintBat()

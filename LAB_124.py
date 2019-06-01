##Sekcja 8, wykład 124
##Kryptografia kojarzy się z informatyką i matematyką,
##tymczasem Czesławowi Miłoszowi przypisuje się autorstwo wiersza
##"Runą w łunach..."
##(więcej szczegółów: http://www.wilnoteka.lt/tresc/jak-milosz-wykiwal-stalina
## - gdyby link nie działał daj mi znać :) )
##Ten sam wiersz czytany w odpowiedni sposób albo wychwala Stalina,
##Armię Czerwoną, Rosję i Kreml, albo przepowiada ich rychły upadek.
##Napiszemy program zmieniający znaczenie wiersza:
##1. Zadeklaruj zmienną poem
##(a przy okazji przeczytaj wiersz i zwróć uwagę na jego znaczenie):
##    poem = '''1.Runą i w łunach spłoną pożarnych 
##    Krzyże kościołów, krzyże ofiarne 
##    I w bezpowrotnym zgubi się szlaku 
##    W lechickiej ziemi Orzeł Polaków. 
##    2.O, jasne słońce- wodzu Stalinie! 
##    Niech sława twoja nigdy nie zginie 
##    Niechaj jak orły powiedzie z gniazda 
##    Rosja i z Kremla płonąca gwiazda. 
##    3.Na ziemskim globie flagi czerwone 
##    Będą na wiatrach grały jak dzwony 
##    Czerwona Armia i wódz jej Stalin 
##    Odwiecznych wrogów na zawsze obali! 
##    4.Zaćmisz się rychło w czarnej godzinie 
##    Polsko- Twe córy i syny, 
##    Wiara i każdy krzyż na mogile, 
##    U stóp am legą w prochu i pyle! '''
##2. Do zmiennej lines zapisz wynik rozbicia napisu
##poem ze względu na znak enter czyli "\n".
##3. Napisz pętlę for wyświetlającą liniję
##pierwszą, dziewiątą, drugą, dziesiątą, trzecią, jedenastą itp.
##Pisząc pętlę for pamiętaj o tym że tak na prawdę mówimy  o linijkach
##0,8,1,9,2,10...
##4. Przeczytaj wygenerowany wiersz
##Prawda, że język polski jest ciekawym przedmiotem?

#1
poem = '''1.Runą i w łunach spłoną pożarnych 
    Krzyże kościołów, krzyże ofiarne 
    I w bezpowrotnym zgubi się szlaku 
    W lechickiej ziemi Orzeł Polaków. 
    2.O, jasne słońce- wodzu Stalinie! 
    Niech sława twoja nigdy nie zginie 
    Niechaj jak orły powiedzie z gniazda 
    Rosja i z Kremla płonąca gwiazda. 
    3.Na ziemskim globie flagi czerwone 
    Będą na wiatrach grały jak dzwony 
    Czerwona Armia i wódz jej Stalin 
    Odwiecznych wrogów na zawsze obali! 
    4.Zaćmisz się rychło w czarnej godzinie 
    Polsko- Twe córy i syny, 
    Wiara i każdy krzyż na mogile, 
    U stóp am legą w prochu i pyle! '''

lines=poem.split("\n")
for i in range(8):
    print(lines[i])
    print(lines[i+8])

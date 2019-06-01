##Sekcja 4, wykład 31
##
##1. Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV.
##Użyj jednego polecenia print
##
##2. Wyświetl w/w teksty używając jako separatora znaku ";"
##
##3. Korzystając z jednego polecenia print wyświetl napis (bez podtekstów!):
##I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV 
##
##4. Zadeklaruj zmienne ProgramName o wartości 'BBC',
##Item o wartości 'News'' i Time o wartości '18:00'. 
##
##5. Uwaga: W tym zadaniu nie używaj konkatenacji napisów (łączenia napisów).
##Użyj tylko polecenia print!
##Wyświetl napis (zwróć uwagę na kropkę na końcu!):
##I like watching News at 18:00 on BBC .
##
##6.  Zmień napis tak, aby kropka była zaraz za  BBC.
##Nadal nie korzystamy z konkatenacji ale z pojedyńczego polecenia print.
#1
print ("TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV")
print ("TVP1", "TVP2", "TVN", "Polsat","BBC", "HBO", "MTV")
#2
print ("TVP1", "TVP2", "TVN", "Polsat","BBC", "HBO", "MTV",sep=';')
#3
print("I like capomputers","TVP1", "TVP2", "TVN",
      "Polsat","BBC", "HBO", "MTV", sep=' but better is ')
#4
ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print ("I like watching",Item, "at","time", "on", ProgramName,".")
#5
print ("I like watching ",Item, " at ","time", " on ", ProgramName,".", sep="")



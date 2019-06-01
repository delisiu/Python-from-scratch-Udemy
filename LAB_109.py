##Sekcja 8, wykład 109
##
##Oto wyniki konkursu Eurowizja 2018 w postaci dwóch list:
##
##    percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
##               2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
##               3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
##               4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
##               8.740978348,6.174819567]
##     
##    countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
##                 'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
##                 'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
##                 'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
##                 'Cyprus','Italy']
##
##Ogólna liczba punktów przyznanych w konkursie to
##sumOfPoints = 4988
##Wyznacz najniższą i najwyższą wartość z listy percent
##Stwórz pętlę for, która wykona się dla zmiennej sterującej
##i między 0 a (długość listy countries minus 1)
##Każdorazowo wyświetl:
##odpowiednią wartość z listy percent
##wartość percent "zrzutowaną" na typ int
##wartość percent zaokrągloną do dwóch miejsc po przecinku
##ilość punktów przyznaną danemu krajowi. Da się to obliczyć,
##bo znamy procentową ilość punktów przyznanych danemu krajowi
##oraz sumaryczną ilość punktów.
##Rzutując wynik na int, otrzymasz go w postaci liczby całkowitej
##nazwę kraju
percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
               2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
               3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
               4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
               8.740978348,6.174819567]
     
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
                 'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
                 'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
                 'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
                 'Cyprus','Italy']

sumOfPoints = 4988
print(min(percent))
print(max(percent))
for i in range (0,len(countries)-1):
#    print(percent[i],int(percent[i]),round(percent[i],2))
    print(int(percent[i]*sumOfPoints/100),countries[i])

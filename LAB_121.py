##Sekcja 8, wykład 121
##1. Rzuć kostką. Co? Nie masz kostki do gry pod ręką? W takim razie:
##    Zaimportuj moduł random
##    Zainicjiuj zmienne min =1 i max = 6
##    Do zmiennej dice zapisz wynik losowania liczby między min, a max.
##    W ten sposób zasymulowaliśmy rzut kostką.
##    Napisz sekwencję poleceń if/elif/else,
##    która w zależności od wylosowanej wartości wyświetli:
##    1:    
##     o 
##    2:
##      o
##      o  
##       3:
##      o
##     o 
##    o  
##    4:
##    o o
##    o o
##    5:
##    o o
##     o 
##    o o
##    6:
##    o o
##    o o
##    o o
##2. Trochę zmieniamy temat. Rzuć pięcioma kostkami:
##    zadeklaruj zmienną dices jako pustą listę
##    pięć razy wylosuj liczbę z zakresu min do max i wynik dopisz do listy dices
##    posortuj listę dices
##    wyświetl zawartość zmienej dices  

#1
import random
min=1
max=6
dice=(random.randint(min,max))
print(dice)

p1='''
    o 
     ''' 
p2='''
    o  
    o  
    '''
p3='''
      o
     o 
    o  
     '''
p4='''
    o o   
    o o
     '''
p5='''
    o o
     o 
    o o
     '''
p6='''
    o o
    o o
    o o
    '''
if dice==1:
    print(p1)
elif dice==2:
    print(p2)
elif dice==3:
    print(p3)
elif dice==4:
    print(p4)
elif dice==5:
    print(p5)
elif dice==6:
    print(p6)
    
#2
dice=[]
for i in range(1, 5): 
    dice.append(random.randint(min,max))
print(dice)
dice.sort()
print(dice)

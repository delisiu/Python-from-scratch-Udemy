##Sekcja 7, wykład 93
##
##Dane są następujące napisy:
##    string_A = '+---+---+---+---+'
##    string_B = '|   |   |   |   |'
##1Korzystając z polecenia FOR wyświetl:
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##    +---+---+---+---+
##2Korzystając z polecenia FOR wyświetl:
##    +---+---+---+---+
##    |   |   |   |   |
##    +---+---+---+---+
##    |   |   |   |   |
##    +---+---+---+---+
##    |   |   |   |   |
##    +---+---+---+---+
##    |   |   |   |   |
##    +---+---+---+---+
##3Korzystając z polecenia FOR wyświetl:
##    x
##    xx
##    xxx
##    xxxx
##    xxxxx
##    xxxxxx
##    xxxxxxx
##    xxxxxxxx
##    xxxxxxxxx
##(wskazówka: aby wyświetli 5 liter x użyj "x" *5
##4Korzystając z polecenia FOR wyświetl:
##    o
##    xx
##    ooo
##    xxxx
##    ooooo
##    xxxxxx
##    ooooooo
##    xxxxxxxx
##    ooooooooo
#1, 2
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range (10):
    print (string_A)
print ("XXXXXXXXXXXXXXXXX")

for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)
#3
gw="x"   
for i in range (10):
    print (gw*i)
    #gw+="x"
#4
kolo="o"
gwi="x"
for i in range (10):
    if i % 2==0:
        print (gwi*i)
    else:
        print (kolo*i)

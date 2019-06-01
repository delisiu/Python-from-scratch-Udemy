##Sekcja 5, wykład 63
##
##Przygotowujesz się do analizy email-marketingu.
##Po każdym zadaniu poniżej wyświetl listę:
##1. Utwórz listę o nazwie marketing z elementami:
##-loyality program
##-client promotion
##-market research
##2. Dodaj do listy element 'public relations'
##3. Wyświetl pozycję numer 3
##4. Wstaw na pozycję numer 2 element 'investor relations'
##5. Chcesz jednak aby lista znajdowała się w zmiennej o nazwie emailMarketing.
##Skopiuj elementy z listy marketing do listy emailMarketing
##6. Posortuj listę emailMarketing
##7. Utwórz nową jednoelementową listę internalEmails.
##Jedyny element to 'internal communication'
##8. Dodaj listę internalEmails do listy emailMarketing
##9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing.
##Podczas wyświetlania tuple zwróć uwagę na nawiasy, z jakich skorzystał Python
#1
marketing=['loyality program', 'client promotion', 'market research']
print(marketing)
#2
marketing.append('public relatins')
print(marketing)
#3
print(marketing[3])
#4
marketing.insert(2,'investor relations')
print(marketing)
#5
emailMarketing=marketing.copy()
print(marketing)
print(emailMarketing)
#6
emailMarketing.sort()
print(emailMarketing)
#7
internalEmails=['internal communication']
print(internalEmails)
#8
emailMarketing.extend(internalEmails)
print(emailMarketing)
#9
tupleEmailMarketing=tuple(emailMarketing)
print(emailMarketing)
print(tupleEmailMarketing)


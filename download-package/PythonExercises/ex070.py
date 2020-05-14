# Create a program that reads the name and price of various products. The program should ask if the user will continue.
# At the end, show: A) What is the total spend on the purchase. B) How many products cost more than US$ 1000.00.
# C) What is the cheapest product name.

cheapest = ''
total = thousand = cont = cheap = 0
print('=-' * 17)
print('{:^34}'.format('MATTHEW`S CLUB'))
print('=-' * 17)
while True:
    product = str(input('Product`s Name: ')).strip().title()
    price = float(input('Price: US$ '))
    cont += 1
    total += price
    if price > 1000:
        thousand += 1
    if cont == 1 or price < cheap:
        cheap = price
        cheapest = product
    print('-' * 35)
    proceed = ' '
    while proceed not in 'YN':
        proceed = str(input('Want to continue? [Y/N] ')).strip().upper()[0]
    print('-' * 35)
    if proceed == 'N':
        break
print('{:-^35}'.format(' END OF PROGRAM '))
print(f'The total purchase was US${total:.2f}.')
print(f'We have {thousand} products costing more than US$1000.00.')
print(f'The cheapest product was the {cheapest} that costs US${cheap:.2f}.')

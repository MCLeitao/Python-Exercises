# Create a program that has a unique tuple with product names and their respective prices, next.
# At the end, show a price list, organizing the data in tabular form.

listing = ('Pencil', 1.75, 'Eraser', 2, 'Notebook', 15.9,
           'Case', 25, 'Protractor', 4.20, 'Compass', 9.99,
           'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.9)
print('--' * 20)
print(f'{"LISTING OF PRICES":^40}')
print('--' * 20)
for position in range(0, len(listing)):
    if position % 2 == 0:
        print(f'{listing[position]:.<30}', end='')
    else:
        print(f'US$ {listing[position]:>6.2f}')
print('--' * 20)

# Develop a program that asks the distance of a trip in miles.
# Calculate the fare price, charging $ 0.50 per mile for trips up to 200 miles and $ 0.45 for longer trips.

import emoji

d = float(input('Enter the trip distance in miles: '))

if d <= 200.00:
    p = d * 0.50
else:
    p = d * 0.45
# p = d * 0.50 if d <= 200 else d * 0.45
print('The fare price is US${:.2f}'.format(p))
print(emoji.emojize('Have a good trip :oncoming_bus:', use_aliases=True))

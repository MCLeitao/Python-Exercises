# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy
# Consider: US$1.00 = R$5.31

r = float(input('How many Brazilian real do you have in your wallet? R$ '))
d = r / 5.31
print('You can buy US${:.2f} dollars'.format(d))

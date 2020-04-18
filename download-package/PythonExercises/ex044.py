# Develop a program that calculates the amount to be paid for a product, considering its normal price and payment terms.
# In cash/check: 10% discount; On the Card: 5% discount; Up to 2 times on the card: normal price; 3 times or more on the
# card: 20% interest.

print('{:=^40}'.format(' PIGLETS STORES '))
n = float(input('Purchase Price: US$ '))
print('PAYMENT METHODS \n[ 1 ] In cash/check \n[ 2 ] On the card \n[ 3 ] 2x on the card \n[ 4 ] 3x or more on the card')
# print('''PAYMENT METHODS
# [ 1 ] In cash/check
# [ 2 ] On the card
# [ 3 ] 2x on the card
# [ 4 ] 3x or more on the card''')
o = int(input('What is the Option? '))
if o == 1:
    print('The final price is US${:.2f}'.format(n * 0.90))
elif o == 2:
    print('The final price is US${:.2f}'.format(n * 0.95))
elif o == 3:
    print('Your purchase will be installments in 2x of {:.2f} INTEREST FREE.'
          '\nThe final price is US${:.2f}'.format(n/2, n))
elif o == 4:
    i = n * 1.20
    p = int(input('How many Parcels? '))
    print('Your purchase will be in installments in {}x of US${:.2f} WITH INTEREST.'
          '\nThe final price is US${:.2f}'.format(p, i/p, i))
else:
    print('\033[1;30;41m Invalid Payment Option. Try Again. \033[m')

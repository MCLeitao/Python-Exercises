# Create a program that simulates the functioning of an ATM. At the beginning, ask the user what will be the amount to
# be withdrawn (whole number) and the program will inform how many bills of each amount will be delivered.
# Consider that the ATM has banknotes of US$50, US$20, US$10 and US$1.

print('=' * 30)
print('{:^30}'.format('MATTHEW`S BANK'))
print('=' * 30)
value = int(input('How much do you want to withdraw? US$'))
bill = 50
totbills = 0
'''cont = 1
while True:
    if cont == 2:
        bill = 20
    elif cont == 3:
        bill = 10
    elif cont == 4:
        bill = 1
    totbills = value // bill
    value -= totbills * bill
    if totbills > 0:
        print(f'Total of {totbills:^} US${bill:^} bills.')
    cont += 1
    if value == 0:
        break'''
# Or:
total = value
while True:
    if total >= bill:
        total -= bill
        totbills += 1
    else:
        if totbills > 0:
            print(f'Total of {totbills:^} US${bill} bills')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totbills = 0
        if total == 0:
            break
#
print('=' * 30)
print('You are welcome back anytime! Have a nice day!')

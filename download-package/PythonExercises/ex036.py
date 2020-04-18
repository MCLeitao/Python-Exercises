# Write a program to approve the bank loan for the purchase of a home.
# The program will ask for the value of the house, the buyer's salary and how many years he will pay.
# Calculate the monthly instalment amount, knowing that it cannot exceed 30% of the salary or the loan will be denied.

from time import sleep

print('-=-' * 10, '\n Welcome to the Loan Analyzer\n', '-=-' * 10)
value = float(input('Value of the House: US$'))
salary = float(input('Your Salary: US$'))
year = int(input('How many years of financing: '))
inst = value / (year * 12)
print('Analyzing ...')
sleep(2)
if inst <= salary * 0.3:
    print('Loan {}APPROVED{}!\nThe Monthly instalment amount is {}US${:.2f}{}'
          .format('\033[1;30;42m', '\033[m', '\033[1;30;41m', inst, '\033[m'))
else:
    print('To pay a house of US${:.2f} in {} years, the installment will be US${:.2f}.'
          '\nLoan \033[1;31;40m DENIED \033[m!'.format(value, year, inst))
print('Have a good day!!')

# Write a program that asks for an employee's salary and calculates the amount of your increase.
# For salaries in excess of US$ 1,250.00, calculate an increase of 10%.
# For those less than or equal, the increase is 15%.

s = float(input('Enter the employees salary: US$ '))

if s > 1250:
    new = s * 1.10
    print('The new salary, whit a increase of 10%, is: US${:.2f}'.format(new))
else:
    new = s * 1.15
    print('The new salary, whit a increase of 15%, is: US${:.2f}'.format(new))

# Write a program that reads a velocity by a car.
# If he exceeds 80 km/h, show a message saying he was fined.
# The fine will cost US$ 7.00 for every mile over the limit

v = float(input('Enter the current speed of the car: '))
f = (v - 80) * 7
if v > 80:
    print('Car speed exceeded the permitted 80 km/h \nThe fine is: {}US${:.2f} {}'.format('\033[1;31;40m', f, '\033[m'))
else:
    print('The car is within the limit')
print('Have a nice day and drive safely!')

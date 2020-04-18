# Make a program that reads the width and height of a wall in meters, calculate its area and the amount of paint needed
# to paint it. Consider that each liter of paint paints an area of 2mˆ2

w = float(input('Wall width in meters? '))
h = float(input('Wall height in meters? '))
a = w * h
p = a / 2

print('The wall area is {}{:.2f}{} m² \nYou will need {}{:.2f}{} l of paint to paint it'
      .format('\033[1;31;40m', a, '\033[m', '\033[1;32;40m', p, '\033[m'))

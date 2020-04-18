# Make a program that reads any angle and shows on the screen the value of the sine, cosine and tangent of that angle

from math import radians, sin, cos, tan

a = float(input('Enter a angle: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('The SINE of this angle is {:.2f} \nThe COSINE of this angle is {:.2f} \nThe TANGENT os this angle is {:.2f}'
      .format(s, c, t))

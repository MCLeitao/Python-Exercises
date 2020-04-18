# Write a program that converts a temperature by typing in degrees Celsius and converting it to degrees Fahrenheit

c = float(input('Type a temperature in degrees Celsius: '))
f = ((c * 9) / 5) + 32
# It doesn't need parentheses due to order of precedence
print('This temperature in Fahrenheit is {}ºF'.format(f))

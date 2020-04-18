# Create a program that reads two numbers and shows the sum between them

n1 = float(input('Enter a number: '))
n2 = float(input('Type another: '))
s = n1 + n2
print('The sun between \033[1;30;41m{:.2f}\033[m and \033[1;31;40m{:.2f}\033[m worth \033[7;31m{:.2f}\033[m !!'
      .format(n1, n2, s))

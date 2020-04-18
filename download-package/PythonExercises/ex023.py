# Make a program that reads a number from 0 to 9999 and shows each of digit separately on the screen

num = int(input('Type a number from 0 to 9999: '))
# n = str(num)
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
print('Thousand: {} \nHundred: {} \nTen: {} \nUnity {}'.format(th, h, t, u))  # .format(n[0], n[1], n[2], n[3])

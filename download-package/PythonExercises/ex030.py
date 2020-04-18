# Create a program that reads an integer and shows on the screen whether it is even or odd


n = int(input('Type a integer: '))
if n % 2 == 0:
    print('The number {} is {} EVEN {}'.format(n, '\033[1;31;40m', '\033[m'))
else:
    print('The number {} is {} ODD {}'.format(n, '\033[7;30m', '\033[m'))


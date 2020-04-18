# Make a program that reads any integer and shows your multiplication table on the screen

n = int(input('Type a integer o see your multiplication table: '))
print('-' * 12)
print('{} x  1 = {}  \n{} x  2 = {}  \n{} x  3 = {} \n{} x  4 = {} \n{} x  5 = {} \n{} x  6 = {} '
      '\n{} x  7 = {} \n{} x  8 = {} \n{} x  9 = {} \n{} x 10 = {}'.format(n, (n*1), n, (n*2), n, (n*3), n, (n*4),
                                                                           n, (n*5), n,  (n*6), n, (n*7), n, (n*8),
                                                                           n, (n*9), n, (n*10)))
print('-' * 12)

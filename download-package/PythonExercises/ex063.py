# Write a program that reads any integer "n" and shows the first "n" elements of a Fibonacci sequence on the screen.
# Ex. 0 ⇢ 1 ⇢ 1 ⇢ 2 ⇢ 3 ⇢ 5 ⇢ 8.

print('-' * 20)
print(' Fibonacci Sequence')
print('-' * 20)
num = int(input('How many terms do you want to show? '))
prev = 0
current = 1
fib = 0
print('~' * 30)
print(f'{prev} ⇢ {current}', end=' ⇢ ')
cont = 3
more = num
total = 0
while more != 0:
    total += more
    while cont <= total:
        fib = prev + current
        print('{}'.format(fib), end=' ⇢ ')
        prev = current
        current = fib
        cont += 1
    print('PAUSE')
    more = int(input('How many more terms? '))
print(f'Sequence ended with {total} terms shown.')
print('~' * 30)

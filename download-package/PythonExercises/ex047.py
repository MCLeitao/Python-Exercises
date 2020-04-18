# Create a program that shows on the screen all the even numbers that are in the range between 1 and 50.

print('All even numbers between 1 and 50 are:')
for c in range(0, 51):
    if c % 2 == 0:
        print(c)
print('END')

# Develop a program that reads 6 integers and shows the sum of only those that are even.
# If the value entered is odd, disregard it.

sum = 0
cont = 0
for c in range(1, 7):
    num = int(input('Enter the {}ª number: '.format(c)))
    if num % 2 == 0:
        sum += num
        cont += 1
print(f'The Sum of the {cont} even Numbers is {sum}.')

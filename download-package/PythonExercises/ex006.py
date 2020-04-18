# Create a program that reads a number and shows your double, triple and square root

n = float(input('Type a number: '))
print('The double is {} \nThe triple is {} \nThe square root is {:.2f}'.format((n * 2), (n * 3), (n ** (1/2))))

# n**(1/2) ou pow(n,(1/2))

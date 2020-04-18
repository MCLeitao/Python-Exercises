# Make an algorithm that reads the price of a product and shows its new price, with 5% discount.

n1 = float(input('Enter product price: US$ '))
n2 = n1 * 0.95
# n2 = n1 - (n1 * 5 / 100)
print('The new price of the product, in the promotion with 5% discount, is US${:.2f}'.format(n2))

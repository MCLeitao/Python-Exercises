# Make a program that reads the weight of five people. At the end, show what was the highest and lowest weight read.

highest = 0
lowest = 0
for reader in range(1, 6):
    weight = float(input(f'{reader}ª person weight: '))
    if reader == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        elif weight < lowest:
            lowest = weight
print(f'The highest weight read was {highest:.2f} kg.')
print(f'The lowest weight read was {lowest:.2f} kg.')

# Make a program that reads the weight of five people. At the end, show what was the highest and lowest weight read.

highest = 0
lowest = 0
for p in range(1, 6):
    weight = float(input('{}ª person weight: '.format(p)))
    if p == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight
print('The highest weight read was {:.2f} kg'.format(highest))
print('The lowest weight read was {:.2f} kg'.format(lowest))

# Make a program that shows on the screen a countdown to the burst of fireworks, going from 10 to 0, with a 1 second
# pause between them.

from time import sleep

print('{:=^58}'.format('\nBurst of Fireworks\n'))
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('Burst of Fireworks!!')

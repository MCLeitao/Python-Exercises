# Make a program that shows on the screen a countdown to the burst of fireworks, going from 10 to 0, with a 1 second
# pause between them.

from time import sleep
import emoji

print('{:=^54}'.format(' Countdown to the Burst of Fireworks '))
for c in range(0, 11):
    print(c)
    sleep(1)
print(emoji.emojize('Burst of Fireworks!!:boom:', use_aliases=True))

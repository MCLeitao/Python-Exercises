# Improve exercise ex061 by asking the user if he wants to show a few more terms.
# The program ends when he says he wants to show 0 terms.

print('{:-^30}'.format(' AP Generator '))
first = int(input('First Term: '))
reason = int(input('Enter Reason: '))
progression = first
cont = 1
more = 10
total = 0
while more != 0:
    total += more
    while cont <= total:
        print('{}'.format(progression), end=' ⇢ ')
        progression += reason
        cont += 1
    print('PAUSE')
    more = int(input('How many more terms? '))
print(f'Progression ended with {total} terms shown.')

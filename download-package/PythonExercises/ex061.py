# Redo exercise ex051, reading the first term and the reason for an arithmetic progression (AP),
# showing the first 10 terms of the progression using the while structure.

print('{:=^30}'.format(' AP Generator '))
first = int(input('First Term: '))
reason = int(input('Reason: '))
progression = first
cont = 1
while cont <= 10:
    print(f'{progression}', end=' ⇢ ')
    progression += reason
    cont += 1
print('END')

# Or using for loop:

'''
eleventh = first + (11 - 1) * reason  # an = first + (n - 1) * reason 
for cont in range(first, eleventh, reason):
    print(f'{progression}', end=' ⇢ ')
    ap += reason
print('END')
'''

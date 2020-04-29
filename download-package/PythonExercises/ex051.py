# Develop a program that reads the first term and the reason for an arithmetic progression.
# At the end, show the first 10 terms of this progression.

print('=' * 22)
print('Arithmetic Progression')
print('=' * 22)
first = int(input('1ª term: '))
reason = int(input('Reason: '))
eleventh = first + (11 - 1) * reason
for progression in range(first, eleventh, reason):
    print(f'{progression}', end=' ⇢ ')
print('END')

# Another way:
"""
progression = 0
for position in range(0, 10):
    progression = first + (reason * position)
    print(f'{progression}', end=' ⇢ ')
print('END')
"""

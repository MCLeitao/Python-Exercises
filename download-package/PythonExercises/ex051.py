# Develop a program that reads the first term and the reason for an arithmetic progression.
# At the end, show the first 10 terms of this progression.

print('=' * 22)
print('Arithmetic Progression')
print('=' * 22)
first = int(input('Enter first Term: '))
reason = int(input('Enter the Reason: '))
ap = 0
for c in range(0, 10):
    ap = first + (reason * c)
    print(ap, end=' → ')
print('END')

# Another way:
# first = int(input('Enter first Term: '))
# reason = int(input('Enter the Reason: '))
# tenth = first + (10 - 1) * reason
# for c in range(first, tenth + reason, reason):
#     print('{}'.format(c), end=' → ')
# print('END')

# Create a program where the user types any expression using parentheses. Your application should analyse whether the
# expression passed is with open and closed parentheses in the correct order.

"""
expression = str(input('Type expression: ')).strip()
terms = list()
for cont in range(0, len(expression)):
    terms.append(expression[cont])
if terms.count('(') == terms.count(')'):
    print('Your expression is valid!')
else:
    print('Your expression is wrong!')
"""
# or
expression = str(input('Type expression: ')).strip()
terms = []
for symbol in expression:
    if symbol == '(':
        terms.append('(')
    elif symbol == ')':
        if len(terms) > 0:
            terms.pop()
        else:
            terms.append(')')
            break
if len(terms) == 0:
    print('Your expression is VALID!')
else:
    print('Your expression is WRONG!')

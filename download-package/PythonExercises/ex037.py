# Write a program that reads any integer and ask the user to choose the conversion base:
# 1 for binary; 2 for octal; 3 for hexadecimal

dec = int(input('Enter a Integer: '))
print('''Choose one of the bases for Conversion:
[ 1 ] Convert to BINARY 
[ 2 ] Convert to OCTAL 
[ 3 ] Convert to HEXADECIMAL''')
con = int(input('Your Option: '))
if con == 1:
    print('{} converted to BINARY is {}'.format(dec, bin(dec)[2:]))
elif con == 2:
    print('{} converted to OCTAL is {}'.format(dec, oct(dec)[2:]))
elif con == 3:
    print('{} converted to HEXADECIMAL is {}'.format(dec, hex(dec)[2:]))
else:
    print('Invalid Choice. Try again.')

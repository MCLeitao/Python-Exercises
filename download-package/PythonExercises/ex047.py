# Create a program that shows on the screen all the even numbers that are in the range between 1 and 50.

print('{:-^101}'.format('\nAll EVEN numbers between 1 and 50\n'))
for cont in range(2, 51, 2):
    # print('.', end='') - To indicate how many times the loop was made
    print(cont, end=' ⇢ ')
print('END')
# Another way:
# Perform more iterations - use more processor capacity
# for cont in range(1, 51):
#     if cont % 2 == 0:
#         print(cont, end=' ⇢ ')
# print('END')

# The great challenge for a programmer is to make code that performs the same function
# while requiring less of the machine.

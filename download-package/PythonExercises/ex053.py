# Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.
# Ex. Never odd or even; Live on time emit no evil; Step on no pets.

phrase = str(input('Enter a Sentence: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = ''
# reverse = together[::-1] - That way you don't need to use the for loop
for letter in range(len(together) - 1, -1, -1):
    reverse += together[letter]
print('The inverse of {} is {}.'.format(together, reverse))
if reverse == together:
    print('We have a PALINDROME!!')
else:
    print('The phrase entered is NOT a palindrome!!')

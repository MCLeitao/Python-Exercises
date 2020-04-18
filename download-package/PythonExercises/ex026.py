# Make a program that reads a sentence on the keyboard and shows: How many times the letter 'A' appears;
# In what position does it appear the first time;  In what positions does it appear the last time.

type = str(input('Enter a phrase: ')).strip().upper().split()
phrase = ' '.join(type)
print('Times that `A` appears: {} \nPosition first time it appears: {} \nPosition last time it appears: {}'
      .format(phrase.count('A'), phrase.find('A') + 1, phrase.rfind('A') + 1))

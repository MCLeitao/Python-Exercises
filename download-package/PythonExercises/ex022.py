# Create a program that reads a person's full name and displays: The name with all uppercase letters; The name with all
# lowercase letters; How many letters in total (without considering spaces);  How many letters have the first name.

name = str(input('Type the full name: ')).strip()
div = name.split()
jo = ''.join(div)
print('All uppercase letters: {} \nAll lowercase letters: {} \nNumber of letters: {} \nNumber of letters first name: {}'
      .format(name.upper(), name.lower(), len(jo), len(div[0])))  # len(name) - name.count(' '), name.find(' ')

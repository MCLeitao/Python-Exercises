# Create a program that reads something on the keyboard and shows on the screen the primitive type and all possible
# information about it.

n = input('Type something: ')
print('The primitive type of this is:', type(n))
print('Only have spaces? {} \nIs it alphabetic? {} \nIs it a number? {} \nIs it alphanumeric {} '
      '\nIs this in uppercase? {} \nIs this in lowercase? {} \nIs it capitalized? {}'.format(n.isspace(), n.isalpha(),
                                                                                             n.isnumeric(), n.isalnum(),
                                                                                             n.isupper(), n.islower(),
                                                                                             n.istitle()))

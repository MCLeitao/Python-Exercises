# Create a program that reads an integer and shows your successor and predecessors on the screen.

n = int(input('Type an integer: '))
s = n + 1
p = n - 1
colors = {'clean': '\033[m',
          'red': '\033[1;31m',
          'green': '\033[1;32m',
          'nred': '\033[7;31;40',
          'bw': '\033[7;30m'}
print('The successor is {}{}{} \nThe predecessor is {}{}{}'.format(colors['red'], s, colors['clean'],
                                                                   colors['green'], p, colors['clean']))

# The use of variables is necessary when we need to use these values again in the code
# Otherwise, using more variables will take up memory space unnecessarily

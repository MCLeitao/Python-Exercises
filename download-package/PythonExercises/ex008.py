# Write a program that reads a value in meters and displays it converted to centimeters and millimeters

n = float(input('Type a value in meters: '))
km = n * 0.001
hm = n * 0.01
dam = n * 0.1
dm = n * 10
cm = n * 100
mm = n * 1000
colors = {'clean': '\033[m', 'red': '\033[1;31;40m', 'nred': '\033[7;31;40m', 'bw': '\033[7;30m',
          'green': '\033[1;32m', 'blue': '\033[4;34m', 'cian': '\033[1;36m'}
print('The value in kilometers is {}{}{} km  \nThe value in hectometer is {}{}{} hm \nThe value in decameter is {}{}{} '
      'dam \nThe value in decimeter {}{}{} dm \nThe value in centimeters is {}{}{} cm\nThe value in millimeters is {}{}'
      '{} mm'.format(colors['red'], km, colors['clean'], colors['nred'], hm, colors['clean'], colors['bw'], dam,
                     colors['clean'], colors['green'], dm, colors['clean'], colors['blue'], cm, colors['clean'],
                     colors['cian'], mm, colors['clean']))

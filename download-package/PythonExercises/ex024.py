# Create a program that reads a name of a city and says whether or not It begins whit the name 'Santo'

city = str(input('Type a name of a city: ')).strip()
# print(city[:5].title == 'Santo')
div = city.title().split()
print('The name begins with Santo: {}'.format('Santo' in div[0]))

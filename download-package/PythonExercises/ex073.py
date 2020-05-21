# Create a tuple filled with the top 20 in the Premier League table, in order of placement. Then show: A)Only the top 5
# B)The last 4 placed in the table; C)An alphabetical list of teams; D)What position on the table is Manchester United.

premier = ('Manchester City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal',
           'Manchester United', 'Wolves', 'Everton', 'Leicester City',
           'West Ham United', 'Watford', 'Crystal Palace', 'Newcastle United',
           'Bournemouth', 'Burnley', 'Southampton', 'Brighton', 'Cardiff City',
           'Fulham', 'Huddersfield Town')
print('-=' * 15)
print(f'Premier League team list: {premier}')
print('--' * 15)
print(f'The top 5 is {premier[0:5]}')
print('--' * 15)
print(f'The last 4 placed is {premier[-4:]}')
print('--' * 15)
print(f'Alphabetical teams: {sorted(premier)}')
print('--' * 15)
print(f'The Manchester United is in {premier.index("Manchester United") + 1}th position.')
print('-=' * 15)

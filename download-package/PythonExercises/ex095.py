# Enhance Ex093 so that it works with multiple players, including a system for viewing details of each player's
# performance.

goals = list()
players_list = list()
player = dict()

while True:
    print('--' * 15)
    player['Name'] = str(input("Player's Name: ")).title()
    matches = int(input(f"How many matches did {player['Name']} play? "))
    goals.clear()
    for cont in range(0, matches):
        goals.append(int(input(f'  How many goals in match {cont + 1}? ')))
    player['Goals'] = goals[:]
    player['Total'] = sum(goals)
    players_list.append(player.copy())
    while True:
        choice = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
        if choice in 'YN':
            break
        print('Error! Answer only Y or N.')
    if choice == 'N':
        break
print('--' * 20)

print('Cod', end=' ')
for key in player.keys():
    print(f'{key:<15}', end='')
print()
print('--' * 20)
for index, player in enumerate(players_list):
    print(f'{index:>3} ', end='')
    for values in player.values():
        print(f'{str(values):<15}', end='')
    print()
print('--' * 20)

while True:
    search = int(input('Show data for which player? (999 to stop) '))
    if search == 999:
        break
    if search < 0 or search > len(players_list):
        print(f'Error! There is no player with code {search}! Try again')
    else:
        print(f"-- SURVEY OF PLAYER {players_list[search]['Name']}:")
        for index, goals in enumerate(players_list[search]['Goals']):
            print(f"   In the game {index + 1} scored {goals} goals.")
    print('--' * 20)

print('<< WELCOME BACK >>')

# Create a program that manages the performance of a football player. The program will read the player's name and
# how many matches he has played. Then It will read the number of goals scored in each match.
# In the end, all of this will be kept in a dictionary, including the total goals scored during the championship.

performance = dict()
goals = list()

performance['Name'] = str(input("Player's Name: "))
performance['Matches'] = int(input(f"How many matches {performance['Name']} played? "))  # matches = ...

for cont in range(0, performance['Matches']):
    goals.append(int(input(f'  How many goals in match {cont + 1}? ')))

performance['Goals'] = goals[:]
performance['Total'] = sum(goals)

print('-=' * 35)
print(performance)
# or:
print('-=' * 35)
for key, value in performance.items():
    print(f'The {key} field has a value of {value}.')
# or:
print('-=' * 35)
print(f"The player {performance['Name']} played {performance['Matches']} matches")
# print(f"The player {performance['Name'] played {len(performance['Goals'])] matches}}")
for index, goal in enumerate(performance['Goals']):
    print(f'  => In match {index + 1}, He scored {goal} goals.')
print(f"It was a total of {performance['Total']} goals")

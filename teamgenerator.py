import random
players = ["Harikesh","Aaditya","Rishi","Janoshan"]
number_of_participants= len(players)
teams=2

while number_of_participants>0 and teams>0:
    team = random.sample(players, int(number_of_participants/teams))
    for x in team:
        players.remove(x)
        number_of_participants -= int(number_of_participants/teams)
        teams -= 1

print(team)


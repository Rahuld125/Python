players = {}
i = 1
while i <= 5:
    name = input("Enter player name: ")
    runs = int(input("Enter runs scored: "))
    players[name] = runs
    i += 1
print(players)
print("Highest score is:", max(players.values()))

import json
filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
player1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'Awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': 'Clinton Hillary',
    'Score': 346,
    'Awards': ['WI', "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers, myfile)
myfile.close()

myfile = open(filename, mode='r')
myData = json.load(myfile)
for user in myData:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Awards: " + str(user['Awards']))

#json.dumps(x, indent=4)
# json.dumps(x, indent=4, separators=(". ", " = "))
# json.dumps(x, indent=4, sort_keys=True)
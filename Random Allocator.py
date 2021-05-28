import random
players = ["Martin", "Craig", "Sue",
           "Claire", "Omar", "Cyla",
           "Luciana", "Harry", "Jack",
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "Willaim",
           "Ada", "Grace", "Jean",
           "Marrissa", "Alan", "Cade", "Anna"]
print("Welcome to Team/Player Allocator!")
while True:
    random.shuffle(players)
    response = input("is it a team or individual sport?\\nType team or individual: ")
    if response =="team":
        Ryders = players[:len(players)//3:]
    print("Ryders captain: " + random.choice(Ryders))
    print("Ryders:")
    for player in Ryders:
        print(player)
        Bandits = players[len(players)//3:(len(players)//3)*2]
    print("\nBandits captain: " + random.choice(Bandits))
    print("Bandits:")
    for player in Bandits:
        print(player)
        Cougars = players[(len(players)//3)*2:]
    print("\nCougars captain: " + random.choice(Cougars))
    print("Cougars:")
    for player in Cougars:
        print(player)
    else:
        for i in range(0, 22, 2):
            print(players[i] + "vs" + players[i+1])
            start = random.randrange(i, i+2)
            print(players[start] + " starts")
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break


  

import random
from random import choice

playing = True

games = int(0)
win_text = "You won"
wins_count = int(0)
lose_text = "You lose"
loses_count = int(0)

while playing:

    things = [
        "rock",
        "paper",
        "scissors",
        "spock",
        "lizard"
    ]

    for i in range(5):
        print(things[i])

    userChoose = input("Select your thing: ").lower()

    if userChoose == "":
        playing = False
        quit()

    botChoose = random.choice(things)

    print("Your choose:", userChoose)
    print("Bot choose:", botChoose)

    def rock():
        global wins_count
        global loses_count
        if botChoose == "scissors" or botChoose == "lizard":
            print(win_text)
            wins_count += 1
        elif botChoose == "rock":
            print("Dead heat")
        else:
            print(lose_text)
            loses_count += 1

    def paper():
        global wins_count
        global loses_count
        if botChoose == "rock" or botChoose == "spock":
            print(win_text)
            wins_count += 1
        elif botChoose == "paper":
            print("Dead heat")
        else:
            print(lose_text)
            loses_count += 1

    def scissors():
        global wins_count
        global loses_count
        if botChoose == "paper" or botChoose == "lizard":
            print(win_text)
            wins_count += 1
        elif botChoose == "scissors":
            print("Dead heat")
        else:
            print(lose_text)
            loses_count += 1

    def spock():
        global wins_count
        global loses_count
        if botChoose == "scissors" or botChoose == "rock":
            print(win_text)
            wins_count += 1
        elif botChoose == "spock":
            print("Dead heat")
        else:
            print(lose_text)
            loses_count += 1

    def lizard():
        global wins_count
        global loses_count
        if botChoose == "spock" or botChoose == "paper":
            print(win_text)
            wins_count += 1
        elif botChoose == "lizard":
            print("Dead heat")
        else:
            print(lose_text)
            loses_count += 1


    if userChoose == "rock":
        rock()
    elif userChoose == "paper":
        paper()
    elif userChoose == "scissors":
        scissors()
    elif userChoose == "spock":
        spock()
    elif userChoose == "lizard":
        lizard()
    else:
        print("Don't enter something else!")

    games += 1
    print("GAMES:", games, "WINS:", wins_count, "LOSES:", loses_count)
    print()


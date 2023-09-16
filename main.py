import random
from random import choice
things = [
    "rock",
    "paper",
    "scissors",
    "spock",
    "lizard"
]

for i in range(5):
    print(things[i])

userChoose = input("Select your thing: ")

botChoose = random.choice(things)

print("Your choose:", userChoose)
print("Bot choose:", botChoose)

def rock():
    if botChoose == "scissors" or botChoose == "lizard":
        print("You won!")
    elif botChoose == "rock":
        print("Dead heat")
    else:
        print("You lose")

def paper():
    if botChoose == "rock" or botChoose == "spock":
        print("You won!")
    elif botChoose == "paper":
        print("Dead heat")
    else:
        print("You lose")

def scissors():
    if botChoose == "paper" or botChoose == "lizard":
        print("You won!")
    elif botChoose == "scissors":
        print("Dead heat")
    else:
        print("You lose")

def spock():
    if botChoose == "scissors" or botChoose == "rock":
        print("You won!")
    elif botChoose == "spock":
        print("Dead heat")
    else:
        print("You lose")

def lizard():
    if botChoose == "spock" or botChoose == "paper":
        print("You won!")
    elif botChoose == "lizard":
        print("Dead heat")
    else:
        print("You lose")


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
# simple game Rock-Paper-Scissors


from random import randint

# create a list of play options
play_options = ['Rock', 'Paper', 'Scissors']
computer = play_options[randint(0, 2)]

player = False
while player == False:

    player = input("Please choose: Rock, Paper or Scissors? ")

    if player == computer:
        print('Tie')
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You won!", player, "smashes", computer)

    elif player == "Paper":
        if computer == "Scissors":
            print("You loose!")
        else:
            print("You win!")

    elif player == "Scissors":
        if computer == "Rock":
            print("You loose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

    else:
        print("That is not a valid move")
    player = False
    computer = play_options[randint(0, 2)]

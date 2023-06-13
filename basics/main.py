import random

def get_choices():
    # player_choice = "rock"
    player_choice = input("Enter a choice (Rock, Paper, Scissors)>>>>")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)

    choice = {"player": player_choice, "computer": computer_choice}

    return choice

def check_win(player_choice, computer_choice):
    print(f"you chose {player_choice} and computer chose {computer_choice}")
    # if player_choice == computer_choice:
    #     return "It's a tie"
    # elif player_choice == "rock" and computer_choice == "scissors":
    #     return "Player Wins"
    # elif player_choice == "rock" and computer_choice == "paper":
    #     return "Computer Wins"

    # TODO cover the other scenarios
    if player_choice == computer_choice:
        return "It's a tie"
    elif player_choice == "rock":
        if computer_choice == "scissors":
            return "Player Wins"
    else:
        return "Computer Wins"





choices = get_choices()

print("result........",check_win(choices["player"], choices["computer"]))

print(choices)

# dict = {"name": "bond", "code": "007", "choices": choices}
# print(dict["name"])
# print(dict["choices"])

# food = ["pizza", "carrots", "eggs"]

# dinner = random.choice(food)
# print("dinner...........", dinner)

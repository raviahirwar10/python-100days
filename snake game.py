#exersice 5
import random

def check_win(player, computer):
    if player ==  computer:
        return "Tie!"
    elif player == "snake" and computer == "water":
        return "You win"
    elif player == "water" and computer == "gun":
        return "You win"
    elif player == "gun" and computer == "snake":
        return "You win"
    else:
        return "Computer wins"
print('Snake, Water, Gun game')
print("Choices: snake/water/gun")

player = input("Enter your choice: ").lower()
computer = random.choice(["snake","water","gun"])

print("computer chose:", computer)
print(check_win(player, computer))
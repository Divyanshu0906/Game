import random
from menu import MOVES, show_menu, get_choice, show_result
from logic import check_winner

def run():
    while True:
        show_menu()
        choice = get_choice()

        if choice == "4":
            print("Thank You!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid input.")
            continue

        player_move   = MOVES[int(choice) - 1]
        computer_move = random.choice(MOVES)
        result        = check_winner(player_move, computer_move)

        show_result(player_move, computer_move, result)
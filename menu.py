MOVES = ["Stone", "Paper", "Scissors"]

def show_menu():
    print("\n--- Start Game ---")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

def get_choice():
    return input("Enter a choice (1-4): ")

def show_result(player_move, computer_move, result):
    print(f"\nYou picked     : {player_move}")
    print(f"Computer picked: {computer_move}")
    print(f"Result         : {result}")
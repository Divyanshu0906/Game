def check_winner(player, computer):

    if player == computer:
        return "It is a tie!"

    elif player == "Stone" and computer == "Scissors":
        return "You win!"

    elif player == "Paper" and computer == "Stone":
        return "You win!"

    elif player == "Scissors" and computer == "Paper":
        return "You win!"

        
    else:
        return "Computer wins!"
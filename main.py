# AI Tic-Tac-Toe using Minimax Algorithm

board = [" "] * 9


def print_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner():
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(is_ai_turn):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_ai_turn:
        best_score = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score


def find_best_move():
    best_score = -100
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    print("===== AI TIC-TAC-TOE =====")
    print("You are X")
    print("AI is O")

    while True:
        print_board()

        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = "X"

        result = check_winner()
        if result is not None:
            print_board()
            break

        # AI move
        print("AI is thinking...")
        ai_move = find_best_move()
        board[ai_move] = "O"

        result = check_winner()
        if result is not None:
            print_board()
            break

    if result == "X":
        print("You won!")
    elif result == "O":
        print("AI won!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
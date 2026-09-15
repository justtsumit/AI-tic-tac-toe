# AI-tic-tac-toe
A simple command-line Tic-Tac-Toe game where an AI player uses the Minimax algorithm to make decisions.
# AI Tic-Tac-Toe using Minimax

## 1. Project Description

This project is a command-line Tic-Tac-Toe game in which a human player plays against an AI.

The player uses `X` and the AI uses `O`. The AI selects its moves using the Minimax algorithm.

The main purpose of this project is to demonstrate how an AI can make decisions in a simple two-player game.

## 2. AI Technique Used

The project uses the Minimax algorithm.

Minimax is a decision-making algorithm used in two-player games. It checks possible future moves and selects a move that gives the best possible result for the AI.

In this project:

* AI is represented by `O`.
* Human player is represented by `X`.
* AI tries to maximize its score.
* The human player is considered as the opponent, so the algorithm tries to minimize the score for the AI.
* A win for AI has a score of `1`.
* A win for the player has a score of `-1`.
* A draw has a score of `0`.

## 3. Requirements

* Python 3.x
* Command-line terminal
* No external Python libraries are required.

## 4. Project Structure

```text
AI-Tic-Tac-Toe/
│
├── main.py
├── README.md
├── requirements.txt
└── report.md
```

## 5. How to Run

### Step 1: Download or clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Tic-Tac-Toe.git
```

### Step 2: Open the project directory

```bash
cd AI-Tic-Tac-Toe
```

### Step 3: Run the program

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## 6. How to Play

The board contains positions from 1 to 9.

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Enter the number of the position where you want to place `X`.

The AI will then calculate its move and place `O`.

The game continues until one player wins or the board becomes full.

## 7. Example Output

```text
===== AI TIC-TAC-TOE =====
You are X
AI is O

   |   |
---+---+---
   |   |
---+---+---
   |   |

Enter your move (1-9): 5

AI is thinking...

   | O |
---+---+---
   | X |
---+---+---
   |   |

Enter your move (1-9):
```

The exact moves can be different because they depend on the player's choices.

## 8. Features

* Human vs AI gameplay
* Minimax-based AI decision making
* Win and draw detection
* Invalid move handling
* Runs completely through the command line
* Does not require an internet connection
* Does not require external libraries

## 9. Limitations

The current version is designed for a simple 3 × 3 Tic-Tac-Toe game.

The AI can take time to calculate because Minimax checks possible future game states.

## 10. Future Scope

The project can be extended by:

* Adding different difficulty levels
* Adding a graphical interface
* Keeping player scores
* Adding a larger board
* Improving the decision-making algorithm

## 11. Conclusion

This project demonstrates the use of artificial intelligence in game playing.

The Minimax algorithm allows the AI to examine possible moves and select a suitable move based on the expected result.

The project helped in understanding decision making, game states, utility values, and adversarial search.
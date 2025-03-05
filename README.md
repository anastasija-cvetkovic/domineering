# Students that contributed to making this project
- Anastasija Cvetković 18033
- Teodora Cvetković 18040
  
# Domineering Game

## Overview
This project is a Python implementation of the classic board game **Domineering**. In Domineering, two players take turns placing domino pieces on a grid:
- **Player X** places dominoes vertically.
- **Player O** places dominoes horizontally.

The game continues until no valid moves remain, and the last player to make a move wins.

## Features
- **Two Modes of Play:**
  - **Human vs Computer:** Play against an AI that uses the minimax algorithm with alpha-beta pruning.
  - **Human vs Human:** Enjoy a two-player game where both moves are manually entered.
- **Customizable Board:** Choose the number of rows and columns to set your desired difficulty and board size.
- **Command-Line Interface:** A clear CLI displays the board, prompts for moves, and handles game logic.
- **Minimax AI:** The computer player evaluates moves using a recursive minimax algorithm enhanced with alpha-beta pruning for efficient decision-making.

## Project Structure
- **domineering.py:**  
  The main entry point. It handles board setup, mode selection (Human vs Computer or Human vs Human), and game initialization.
  
- **board.py:**  
  Contains the `Board` class responsible for:
  - Creating and drawing the board.
  - Validating moves for both players.
  - Applying moves and undoing them when necessary.
  - Evaluating board positions.
  
- **base_player.py:**  
  Defines the base `Player` class used by both human and computer players.

- **players.py:**  
  Implements:
  - `HumanPlayer`: Handles user input and move validation.
  - `ComputerPlayer`: Uses the minimax algorithm to choose optimal moves.
  
- **game.py:**  
  Manages the game loop, alternating between players and checking for game termination conditions.

- **minimax.py:**  
  Implements the minimax algorithm with alpha-beta pruning to help the computer determine the best possible move.

- **common.py:**  
  Contains shared constants and variables such as player markers and infinity values for the minimax algorithm.

## Installation
1. **Prerequisites:**  
   Ensure you have Python 3.x installed on your system.

2. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-username/domineering-game.git

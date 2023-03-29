# Overview

I created this project as part of CS111 (Introduction to Computer Science 1) at Boston University. It uses object-oriented programming in order to create a working Connect 4 in Python. A user can play against another user or AI, and the game will result in either a win, loss, or tie.

# Files

The game.py file is what allows the user to play the game. It initializes all of the conditions, and processes any moves that the user(s), random player, or AI make. It also defines a random player class, an opponent that always plays the game at random. The board.py file creates a board class, which defines the Connect 4 board, the moves of the game, and evaluates the outcome of the game. The player.py file creates the player class, defining the checker in use and allowing the user(s) to input a move. Finally, the ai.py file creates an AI player class. The AI difficulty is set by defining how many moves ahead the AI can look (implemented using recursive backtracking). 

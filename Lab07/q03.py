import random
import numpy as np

class Battleship:
    def __init__(self):
        self.board_size = 10
        self.player_board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.ai_board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.player_guesses = np.zeros((self.board_size, self.board_size), dtype=int)
        self.ai_guesses = np.zeros((self.board_size, self.board_size), dtype=int)
        self.ships = {
            'Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2
        }
        self.initialize_boards()

    def initialize_boards(self):
        # Place ships for both players
        self.place_ships(self.player_board)
        self.place_ships(self.ai_board)

    def place_ships(self, board):
        for ship_name, ship_size in self.ships.items():
            while True:
                # Randomly choose orientation (0 for horizontal, 1 for vertical)
                orientation = random.randint(0, 1)
                
                if orientation == 0:  # Horizontal
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - ship_size)
                    if all(board[row][col + i] == 0 for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row][col + i] = 1
                        break
                else:  # Vertical
                    row = random.randint(0, self.board_size - ship_size)
                    col = random.randint(0, self.board_size - 1)
                    if all(board[row + i][col] == 0 for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row + i][col] = 1
                        break

    def print_board(self, board, hide_ships=False):
        print("  A B C D E F G H I J")
        for i in range(self.board_size):
            print(f"{i}", end=" ")
            for j in range(self.board_size):
                if hide_ships and board[i][j] == 1:
                    print(".", end=" ")
                elif board[i][j] == 0:
                    print(".", end=" ")
                elif board[i][j] == 1:
                    print("S", end=" ")
                elif board[i][j] == 2:
                    print("X", end=" ")
                elif board[i][j] == 3:
                    print("O", end=" ")
            print()

    def get_coordinates(self, coord_str):
        try:
            col = ord(coord_str[0].upper()) - ord('A')
            row = int(coord_str[1:])
            if 0 <= row < self.board_size and 0 <= col < self.board_size:
                return row, col
        except:
            pass
        return None

    def calculate_probability_grid(self):
        probability_grid = np.zeros((self.board_size, self.board_size))
        
        # For each cell
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.ai_guesses[i][j] != 0:  # Skip already guessed cells
                    continue
                
                # Check horizontal possibilities
                for ship_size in self.ships.values():
                    for k in range(ship_size):
                        if j - k >= 0 and j - k + ship_size <= self.board_size:
                            if all(self.ai_guesses[i][j - k + l] == 0 for l in range(ship_size)):
                                for l in range(ship_size):
                                    probability_grid[i][j - k + l] += 1
                        
                        if i - k >= 0 and i - k + ship_size <= self.board_size:
                            if all(self.ai_guesses[i - k + l][j] == 0 for l in range(ship_size)):
                                for l in range(ship_size):
                                    probability_grid[i - k + l][j] += 1
        
        return probability_grid

    def get_ai_move(self):
        probability_grid = self.calculate_probability_grid()
        
        # Find cells with highest probability
        max_prob = np.max(probability_grid)
        if max_prob > 0:
            high_prob_cells = np.where(probability_grid == max_prob)
            idx = random.randint(0, len(high_prob_cells[0]) - 1)
            return high_prob_cells[0][idx], high_prob_cells[1][idx]
        
        # If no high probability cells, choose random unguessed cell
        unguessed = np.where(self.ai_guesses == 0)
        idx = random.randint(0, len(unguessed[0]) - 1)
        return unguessed[0][idx], unguessed[1][idx]

    def make_guess(self, board, guesses, row, col):
        if guesses[row][col] != 0:
            return False, "Already guessed this position!"
        
        if board[row][col] == 1:
            board[row][col] = 2  # Hit
            guesses[row][col] = 2
            return True, "Hit!"
        else:
            guesses[row][col] = 3  # Miss
            return True, "Miss!"

    def check_winner(self, board):
        return not np.any(board == 1)

    def play(self):
        print("Welcome to Battleship!")
        print("\nYour board (S = Ship):")
        self.print_board(self.player_board)
        print("\nAI's board (hidden):")
        self.print_board(self.ai_board, hide_ships=True)
        
        while True:
            # Player's turn
            while True:
                try:
                    coord = input("\nEnter your guess (e.g., A5): ")
                    row, col = self.get_coordinates(coord)
                    if row is None or col is None:
                        print("Invalid coordinates! Try again.")
                        continue
                    
                    success, message = self.make_guess(self.ai_board, self.player_guesses, row, col)
                    if not success:
                        print(message)
                        continue
                    
                    print(f"Player attacks: {coord} → {message}")
                    break
                except:
                    print("Invalid input! Try again.")
            
            if self.check_winner(self.ai_board):
                print("\nCongratulations! You won!")
                break
            
            # AI's turn
            ai_row, ai_col = self.get_ai_move()
            success, message = self.make_guess(self.player_board, self.ai_guesses, ai_row, ai_col)
            print(f"AI attacks: {chr(ai_col + ord('A'))}{ai_row} → {message}")
            
            if self.check_winner(self.player_board):
                print("\nAI won! Better luck next time!")
                break
            
            # Print updated boards
            print("\nYour board:")
            self.print_board(self.player_board)
            print("\nAI's board:")
            self.print_board(self.ai_board, hide_ships=True)

if __name__ == "__main__":
    game = Battleship()
    game.play() 
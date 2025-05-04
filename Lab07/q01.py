import numpy as np
from colorama import init, Fore, Style

init()  # Initialize colorama

class Checkers:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)
        self.initialize_board()
        self.current_player = 1  # 1 for white (human), -1 for black (AI)
        
    def initialize_board(self):
        # Place black pieces (-1)
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 1:
                    self.board[i][j] = -1
        
        # Place white pieces (1)
        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    self.board[i][j] = 1

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(f"{i}", end=" ")
            for j in range(8):
                if self.board[i][j] == 0:
                    print(".", end=" ")
                elif self.board[i][j] == 1:
                    print(f"{Fore.WHITE}W{Style.RESET_ALL}", end=" ")
                else:
                    print(f"{Fore.BLACK}B{Style.RESET_ALL}", end=" ")
            print()

    def get_valid_moves(self, row, col):
        moves = []
        piece = self.board[row][col]
        
        # Check diagonal moves
        directions = [(1, 1), (1, -1)] if piece == 1 else [(-1, 1), (-1, -1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if self.board[new_row][new_col] == 0:
                    moves.append((new_row, new_col))
                elif self.board[new_row][new_col] == -piece:
                    jump_row, jump_col = new_row + dr, new_col + dc
                    if 0 <= jump_row < 8 and 0 <= jump_col < 8 and self.board[jump_row][jump_col] == 0:
                        moves.append((jump_row, jump_col))
        
        return moves

    def make_move(self, from_pos, to_pos):
        row, col = from_pos
        new_row, new_col = to_pos
        self.board[new_row][new_col] = self.board[row][col]
        self.board[row][col] = 0
        
        # Handle capture
        if abs(new_row - row) == 2:
            capture_row = (row + new_row) // 2
            capture_col = (col + new_col) // 2
            self.board[capture_row][capture_col] = 0

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == 1:
                        moves = self.get_valid_moves(i, j)
                        for move in moves:
                            # Make move
                            original = self.board.copy()
                            self.make_move((i, j), move)
                            
                            eval = self.minimax(depth - 1, alpha, beta, False)
                            
                            # Undo move
                            self.board = original
                            
                            max_eval = max(max_eval, eval)
                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == -1:
                        moves = self.get_valid_moves(i, j)
                        for move in moves:
                            # Make move
                            original = self.board.copy()
                            self.make_move((i, j), move)
                            
                            eval = self.minimax(depth - 1, alpha, beta, True)
                            
                            # Undo move
                            self.board = original
                            
                            min_eval = min(min_eval, eval)
                            beta = min(beta, eval)
                            if beta <= alpha:
                                break
            return min_eval

    def evaluate_board(self):
        score = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    score += 1
                elif self.board[i][j] == -1:
                    score -= 1
        return score

    def get_ai_move(self):
        best_score = float('inf')
        best_move = None
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == -1:
                    moves = self.get_valid_moves(i, j)
                    for move in moves:
                        # Make move
                        original = self.board.copy()
                        self.make_move((i, j), move)
                        
                        score = self.minimax(3, float('-inf'), float('inf'), True)
                        
                        # Undo move
                        self.board = original
                        
                        if score < best_score:
                            best_score = score
                            best_move = ((i, j), move)
        
        return best_move

    def play(self):
        while True:
            self.print_board()
            
            if self.current_player == 1:  # Human's turn
                while True:
                    try:
                        print("\nYour turn (White)")
                        from_row = int(input("Enter row of piece to move: "))
                        from_col = int(input("Enter column of piece to move: "))
                        to_row = int(input("Enter destination row: "))
                        to_col = int(input("Enter destination column: "))
                        
                        if self.board[from_row][from_col] != 1:
                            print("Invalid piece selection!")
                            continue
                            
                        moves = self.get_valid_moves(from_row, from_col)
                        if (to_row, to_col) not in moves:
                            print("Invalid move!")
                            continue
                            
                        self.make_move((from_row, from_col), (to_row, to_col))
                        break
                    except (ValueError, IndexError):
                        print("Invalid input! Try again.")
            
            else:  # AI's turn
                print("\nAI's turn (Black)")
                ai_move = self.get_ai_move()
                if ai_move:
                    from_pos, to_pos = ai_move
                    self.make_move(from_pos, to_pos)
                    print(f"AI moves: {from_pos} → {to_pos}")
                else:
                    print("No valid moves for AI!")
                    break
            
            self.current_player *= -1
            
            # Check for game over
            if self.check_game_over():
                break

    def check_game_over(self):
        white_pieces = np.sum(self.board == 1)
        black_pieces = np.sum(self.board == -1)
        
        if white_pieces == 0:
            print("Black (AI) wins!")
            return True
        elif black_pieces == 0:
            print("White (Human) wins!")
            return True
        return False

if __name__ == "__main__":
    game = Checkers()
    game.play() 
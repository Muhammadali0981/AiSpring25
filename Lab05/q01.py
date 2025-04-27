import chess
import random

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value
    return score

def beam_search(board, beam_width, depth_limit):
    def get_best_moves(board, num_moves):
        moves = list(board.legal_moves)
        move_scores = []
        
        for move in moves:
            board.push(move)
            score = evaluate_board(board)
            board.pop()
            move_scores.append((move, score))
        
        return sorted(move_scores, key=lambda x: x[1], reverse=True)[:num_moves]
    
    def search_recursive(board, depth, beam_width):
        if depth == 0:
            return [], evaluate_board(board)
        
        best_moves = get_best_moves(board, beam_width)
        best_sequence = []
        best_score = float('-inf')
        
        for move, _ in best_moves:
            board.push(move)
            sequence, score = search_recursive(board, depth - 1, beam_width)
            board.pop()
            
            if score > best_score:
                best_score = score
                best_sequence = [move] + sequence
        
        return best_sequence, best_score
    
    return search_recursive(board, depth_limit, beam_width)

board = chess.Board()
beam_width = 3
depth_limit = 3

sequence, score = beam_search(board, beam_width, depth_limit)
print(f"Best move sequence: {[str(move) for move in sequence]}")
print(f"Evaluation score: {score}")


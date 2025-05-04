class CardGame:
    def __init__(self, cards):
        self.cards = cards
        self.max_score = 0
        self.min_score = 0
        self.current_player = "Max"  # Max goes first

    def minimax(self, cards, depth, alpha, beta, is_maximizing):
        if not cards:
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            # Try taking left card
            left_eval = cards[0] + self.minimax(cards[1:], depth + 1, alpha, beta, False)
            max_eval = max(max_eval, left_eval)
            alpha = max(alpha, left_eval)
            
            # Try taking right card
            right_eval = cards[-1] + self.minimax(cards[:-1], depth + 1, alpha, beta, False)
            max_eval = max(max_eval, right_eval)
            alpha = max(alpha, right_eval)
            
            if beta <= alpha:
                return max_eval
            return max_eval
        else:
            min_eval = float('inf')
            # Try taking left card
            left_eval = self.minimax(cards[1:], depth + 1, alpha, beta, True)
            min_eval = min(min_eval, left_eval)
            beta = min(beta, left_eval)
            
            # Try taking right card
            right_eval = self.minimax(cards[:-1], depth + 1, alpha, beta, True)
            min_eval = min(min_eval, right_eval)
            beta = min(beta, right_eval)
            
            if beta <= alpha:
                return min_eval
            return min_eval

    def get_best_move(self, cards):
        left_score = cards[0] + self.minimax(cards[1:], 0, float('-inf'), float('inf'), False)
        right_score = cards[-1] + self.minimax(cards[:-1], 0, float('-inf'), float('inf'), False)
        
        if left_score >= right_score:
            return 0  # Take left card
        return -1  # Take right card

    def play(self):
        print(f"Initial Cards: {self.cards}")
        
        while self.cards:
            if self.current_player == "Max":
                # Max's turn using minimax
                move = self.get_best_move(self.cards)
                card = self.cards.pop(move)
                self.max_score += card
                print(f"Max picks {card}, Remaining Cards: {self.cards}")
                self.current_player = "Min"
            else:
                # Min's turn - always takes the lowest value
                if self.cards[0] <= self.cards[-1]:
                    card = self.cards.pop(0)
                else:
                    card = self.cards.pop()
                self.min_score += card
                print(f"Min picks {card}, Remaining Cards: {self.cards}")
                self.current_player = "Max"

        print(f"\nFinal Scores - Max: {self.max_score}, Min: {self.min_score}")
        if self.max_score > self.min_score:
            print("Winner: Max")
        elif self.min_score > self.max_score:
            print("Winner: Min")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    # Example game with the sample cards
    cards = [4, 10, 6, 2, 9, 5]
    game = CardGame(cards)
    game.play() 
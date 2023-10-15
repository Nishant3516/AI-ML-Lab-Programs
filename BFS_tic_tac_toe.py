from collections import deque

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']
        self.queue = deque([(player, 0) for player in self.players])
        self.moves = [(i, j) for i in range(3) for j in range(3)]

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        return all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3))

    def is_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def make_move(self, player, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        else:
            return False

    def play_game(self):
        while True:
            self.print_board()
            player, move = self.queue.popleft()
            print(f"Player {player}, enter your move (row and column, e.g., '0 0' for the top-left cell):")
            while True:
                try:
                    row, col = map(int, input().split())
                    if 0 <= row < 3 and 0 <= col < 3:
                        if self.make_move(player, row, col):
                            break
                        else:
                            print("Invalid move. Try again.")
                    else:
                        print("Invalid input. Row and column must be between 0 and 2.")
                except ValueError:
                    print("Invalid input. Enter two integers for row and column.")
            if self.is_winner(player):
                self.print_board()
                print(f"Player {player} wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break
            self.queue.append((player, move + 1))

# Example usage:
game = TicTacToe()
game.play_game()

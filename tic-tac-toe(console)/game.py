import player


class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        # we will use single list to rep 3x3 matrix.for this we use list  comprehension
        self.current_winner = None

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[j * 3:(j + 1) * 3] for j in range(3)]:
            print("| " + ' | '.join(row) + ' |')

   
    def print_board_numbers(self):
        # 0|1|2 etc.  telling us what number corresponds to what box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + ' | '.join(row) + ' |')

    def available_moves(self):
        # return empty spot in board
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_square(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move then make the move (assign  square to letter)
        # then return True if valid ir invalid return  False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if same letter three in a row anywhere
        # for rows check
        row_i = square // 3
        row = self.board[row_i * 3:(row_i + 1) * 3]
        """ all(iterable object) -> Return True if bool(x) is True for all values x in the iterable.
            If the iterable is empty, return True.
        """
        if all([spot == letter for spot in row]):
            return True
        # check columns
        col_i = square % 3
        col = [self.board[col_i + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        # for diagonal
        if square % 2 == 0:
            d1 = [self.board[i] for i in [0, 4, 8]]  # left diagonal
            if all([spot == letter for spot in d1]):
                return True
            d2 = [self.board[i] for i in [2, 4, 6]]  # right diagonal
            if all([spot == letter for spot in d2]):
                return True
        return False  # if any of the above condition doesn't satisfy then return False i,e not a winner


def play(game, x_player, o_player, print_game=True):
    # return the winner if or none (tie)
    if print_game:
        game.print_board_numbers()
    letter = 'x'
    # iterate through till box has empty squares
    # (we don't have to worry about winners because we wil just return that which breaks the loop
    while game.empty_square():
        # get the move for the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print("{[0->1st box ] [1->2nd box] [2->3rd box] [3->4th box] [4->5th box] [5->6th box] [6->7th box] ["
                      "7->8th box]}\n "
                      + letter + f' makes a move to the square {square}')
                game.print_board()
                print(" ")
        if game.current_winner:
            if print_game:
                print(letter + " wins :)")
            return letter

        # after we made our move we need to alternate move
        letter = 'o' if letter == 'x' else 'x'
    
    if print_game:
        print("its a tie :)")


# code fragmentation (to run our application  on cmd line)
if __name__ == '__main__':
    x_player = player.HumanPlayer('x')
    o_player = player.RandomComputerPlayer('o')
    ttt = TicTacToe()
    play(ttt, x_player, o_player,0)

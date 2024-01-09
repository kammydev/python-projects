from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 
        self.CurrentWinner = None

    def printboard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | ' .join(row) + ' |')

    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' | ' .join(row) + ' |')

    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def emptysquares(self):
        return ' ' in self.board
    
    def numEmptySquares(self):
        return self.board.count(' ')
    
    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.CurrentWinner = letter
            return True
        return False
    
    def winner(self, square, letter):
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        colInd = square % 3
        column = [self.board[colInd+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False


def play(Game , xplayer, oplayer, printgame=True):
    if printgame:
        Game.printBoardNums()

        letter = 'X'

        while Game.emptysquares():
            if letter == 'O':
                square = oplayer.getMove(Game)
            else:
                square = xplayer.getMove(Game)

            if Game.makeMove(square, letter):
                if printgame:
                    print(letter + f' makes a move to square {square}')
                    Game.printboard()
                    print(' ')

                if Game.CurrentWinner:
                    if printgame:
                        print(f'{letter} wins')
                    return letter
        
                if letter == 'X':
                    letter = 'O'

                else:
                    letter = 'X'

        if printgame:
            print('it\'s a tie')

if __name__ == '__main__':
    xplayer = HumanPlayer('X')
    oplayer = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, xplayer, oplayer, printgame=True)
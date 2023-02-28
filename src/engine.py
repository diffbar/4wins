# Game Engines

#
# This is the murx engine
#    it makes murx


class murx:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        # Initialize game Board
        self.board = [[0] * width for x in range(height)]
        self.nextPlayer = 'X'
        self.won = False
        self.winner = ''


    def playerDrop(self, row):
        if row < 0 or row >= self.width:
            return False # index out if range

        i = 0
        for i in range(self.height):
            if self.board[i][row] != 0:
                continue

            self.board[i][row] = self.nextPlayer
            self.nextPlayer = ('X' if self.nextPlayer == 'O' else 'O' )
            break

    def winningCondition(self):
        #rows
        allSame = lambda a: True if a.count(a[0]) == len(a) else False

        for i in range(self.height):
            t = [self.board[i][x] for x in range(4)]
            if allSame(t) and t[0] != 0:
                return t[0]


        return -1



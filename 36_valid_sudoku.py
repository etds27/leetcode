class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board

        for i in range(len(self.board)):
            row = self.rowAt(i)
            if not len(row) == len(set(row)):
                return False

        for i in range(len(self.board[0])):
            col = self.colAt(i)
            if not len(col) == len(set(col)):
                return False

        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                box = self.boxAt(i, j)
                if not len(box) == len(set(box)):
                    return False
        return True

    def rowAt(self, num):
        return [n for n in self.board[num] if n != "."]

    def colAt(self, num):
        return [self.board[i][num] for i in range(len(self.board)) if self.board[i][num] != "."]

    def boxAt(self, row, col):
        return [self.board[row * 3 + i][col * 3 + j] for i in range(3) for j in range(3) if self.board[row * 3 + i][col * 3 + j] != "."]

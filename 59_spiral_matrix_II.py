class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for i in range(n)]

        i = 1
        row = 0
        col = 0
        d_row = 0
        d_col = 1
        while i <=   n**2:
            n_col = col + d_col
            n_row = row + d_row

            matrix[row][col] = i

            i += 1

            if not (0 <= n_row < len(matrix)) or not (0 <= n_col < len(matrix)) or matrix[n_row][n_col] is not None:
                if d_col == 1:
                    d_col = 0
                    d_row = 1
                elif d_col == -1:
                    d_col = 0
                    d_row = -1
                elif d_row == 1:
                    d_col = -1
                    d_row = 0
                elif d_row == -1:
                    d_col = 1
                    d_row = 0


            col += d_col
            row += d_row
        return matrix
        

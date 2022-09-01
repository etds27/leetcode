import pprint
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat) - 1
        col = 0
        for i in range(len(mat) - 1, -1, -1):
            array = []

            dist = min(len(mat) - i, len(mat[0]))

            for delta in range(dist):
                array.append(mat[i + delta][col + delta])

            array = sorted(array)

            for delta in range(dist):
                mat[i + delta][col + delta] = array[delta]

            # pprint.pprint(mat)

        for i in range(len(mat[0])):
            array = []

            dist = min(len(mat), len(mat[0]) - i)

            for delta in range(dist):
                # print(delta, i + delta)
                array.append(mat[delta][i + delta])

            array = sorted(array)

            for delta in range(dist):
                mat[delta][i + delta] = array[delta]

            # pprint.pprint(mat)
        return mat
        

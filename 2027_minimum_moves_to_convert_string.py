class Solution:
    def minimumMoves(self, s: str) -> int:
        ns = ""
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == "O":
                ns += "O"
            else:
                ns += "OOO"
                moves += 1
                i += 2

            i += 1

        return moves
        


class Solution:

    def shortestSequence(self, rolls: List[int], k: int) -> int:
        collection = set()
        seq_len = 0

        for roll in rolls:
            if roll not in collection:
                collection.add(roll)
                if len(collection) == k:
                    collection = set()
                    seq_len += 1

        return seq_len + 1








    """
    My initial "solution"

    It works correctly but is much slower than the efficient solution

    My solution finds the minimum index for all sequences of each length and then determines the next min index by reading in the list starting from the previous min index and looking for a value v

    Reading other solutions online, I found that looking for all subsequences individually is overly complicated
    instead, I should have looked for all values 1..k and found the min index for that. Then perform the same search starting from min index



    def shortestSequence(self, rolls: List[int], k: int) -> int:
        sequence_memo = {}
        #print(sequence_memo)

        seq = ()
        sequence_memo[0] = {seq: 0}
        iterations = 0

        while True:
            for seq_len in range(1, len(rolls)):
                sequence_memo[seq_len] = {}
                # print()
                # print(seq_len)
                # print()
                for seq, min_idx in sequence_memo[seq_len - 1].items():
                    for i in range(1, k + 1):
                        # print("Current seq, val | %s, %i" % (str(seq), i))
                        new_min_idx = self.shortestSequenceHelper(rolls, min_idx, i)
                        # print(new_min_idx)
                        if new_min_idx == -1:
                            return seq_len

                        new_seq = seq + tuple([i])
                        sequence_memo[seq_len][new_seq] = new_min_idx

                # print(sequence_memo)
            return k

        return k


    def shortestSequenceHelper(self, rolls, min_idx, val):
        # print("Searching for %i in %s" % (val, str(rolls[min_idx:])))
        for c, roll in enumerate(rolls[min_idx:]):
            if roll == val:
                return min_idx + 1 + c

        return -1
    """

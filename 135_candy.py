class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_dist = [1] * len(ratings)
        right_dist = [1] * len(ratings)

        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                left_dist[i + 1] = left_dist[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1]  > ratings[i]:
                right_dist[i - 1] = right_dist[i] + 1


        total = 0
        for candy in [max(l, r) for l, r in zip(left_dist, right_dist)]:
            total += candy

        return total
        

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = {i: (set(), set()) for i in range(1, n + 1)}
        for trust_connection in trust:
            trust_map[trust_connection[0]][0].add(trust_connection[1])
            trust_map[trust_connection[1]][1].add(trust_connection[0])

        potential_judge = None
        for person in trust_map.keys():
            if not len(trust_map[person][0]):
                if potential_judge is not None:
                    return -1

                potential_judge = person


        if potential_judge is None:
            return -1
        if len(trust_map[potential_judge][1]) == len(trust_map) - 1:
            return potential_judge
        return -1

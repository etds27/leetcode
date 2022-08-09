
import sys
class Solution:


    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i: set() for i in range(1, n + 1)}

        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])

        # print("MAP MADE")

        min_deg = 1000000

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                for k in range(j, n + 1):
                    if j in nodes[i] and k in nodes[i] and k in nodes[j]:
                        min_deg = min(min_deg, len(nodes[i]) - 2 + len(nodes[j]) - 2 + len(nodes[k]) - 2)

        """
        My solution which works better for maps with less edges
        for i in range(1, n + 1):
            for j in nodes[i]:
                inter = nodes[i].intersection(nodes[j])

                for k in inter:
                    min_deg = min(min_deg, len(nodes[i]) - 2 + len(nodes[j]) - 2 + len(nodes[k]) - 2)
                    # trios.add(tuple(sorted([i, j, k])))
        """
        if min_deg == 1000000:
            return -1
        return min_deg
        

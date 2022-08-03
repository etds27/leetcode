class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        self.heap = []


        i = 0

        for row in matrix:
            for val in row:
                # print()
                # print(val)
                # print(self.heap)
                # Build initial heap
                if i < k:
                    self.insertHeap(val)
                    i += 1
                elif val < self.heap[0]:
                    self.popHeap()
                    self.insertHeap(val)

        ret = self.popHeap()

        return ret

    def insertHeap(self, val):
        self.heap.append(val)
        # print(val)
        if len(self.heap) == 1:
            return


        current_idx = len(self.heap) - 1
        parent_idx = self.getParentIdx(current_idx)
        while self.heap[current_idx] > self.heap[parent_idx]:
            self.heap[current_idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[current_idx]

            current_idx, parent_idx = parent_idx, self.getParentIdx(parent_idx)

            if parent_idx == -1:
                break

        # print("insert", self.heap)

    def popHeap(self):
        if len(self.heap) == 1:
            return self.heap.pop(-1)

        val = self.heap[0]
        self.heap[0] = self.heap.pop(-1)

        current_idx = 0
        left_idx = 1
        right_idx = 2
        side = False #left
        while True:
            # print("\t", self.heap)

            if left_idx >= len(self.heap):
                break
            elif right_idx >= len(self.heap):
                side = False
            elif self.heap[left_idx] > self.heap[right_idx]:
                side = False
            else:
                side = True

            good_idx = right_idx if side else left_idx


            if self.heap[good_idx] > self.heap[current_idx]:
                self.heap[current_idx], self.heap[good_idx] = self.heap[good_idx], self.heap[current_idx]
            else:
                break

            current_idx = good_idx
            left_idx = self.getLeftIdx(good_idx)
            right_idx = left_idx + 1

        return val






    def getParentIdx(self, idx):
        return (idx - 1) // 2

    def getLeftIdx(self, idx):
        return 2 * idx + 1

    def getRightIdx(self, idx):
        return 2 * idx + 2

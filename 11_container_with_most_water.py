class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        offset = 0
        max_area = min(height[i], height[j]) * (j - i)


        while i < j:
            offset = 0
            # print(i, height[i], j, height[j], height, max_area)

            if height[i] < height[j]:
                # print("Searching left")
                while height[i] >= height[i + offset]:
                    offset += 1

                    if i + offset == len(height):
                        break

                i += offset
                # print("Updating left from %i (%i) to %i (%i)" % (height[i], i, height[i + offset], i + offset))
            else:

                # print("Searching right")

                while height[j] >= height[j - offset]:
                    offset += 1
                    if j - offset == i:
                        break

                j -= offset
                # print("Updating right from %i (%i) to %i (%i)" % (height[j], j, height[j - offset], j - offset))



            max_area = max(max_area, min(height[i], height[j]) * (j - i))

        return max_area

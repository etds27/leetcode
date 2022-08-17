class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_spots = []
        for i, num in enumerate(nums):
            if num % 2:
                odd_spots.append(i)

        # print(odd_spots)

        substrings = 0
        i = 0
        for i in range(len(odd_spots) - (k - 1)):
            start_idx = i
            end_idx = i + k - 1

            #print(start_idx, end_idx, odd_spots[start_idx], odd_spots[end_idx])

            if start_idx == 0:
                l_area = odd_spots[start_idx] + 1
            else:
                l_area = odd_spots[start_idx] - odd_spots[start_idx - 1]

            if end_idx == len(odd_spots) - 1:
                r_area = len(nums) - odd_spots[end_idx]
            else:
                r_area = odd_spots[end_idx + 1] - odd_spots[end_idx]

            substrings += (l_area * r_area)
            # print(start_idx, end_idx, l_area, r_area, l_area * r_area, substrings)
        return substrings

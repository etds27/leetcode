class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for item in arr:
            counter.setdefault(item, 0)
            counter[item] += 1

        removed = 0
        ret_set = set()
        for k, v in sorted(counter.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):

            if removed >= len(arr) // 2:
                return len(ret_set)

            removed += v
            ret_set.add(k)

        return len(ret_set)

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)

        for num in nums:
            counts[num] += 1

        h = []
        for num in counts:
            h.append((counts[num], num))
        
        x = heapq.nlargest(k, h)

        ret = []
        for num in x:
            ret.append(num[1])

        return ret
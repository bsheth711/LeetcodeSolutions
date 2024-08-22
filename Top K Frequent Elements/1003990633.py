class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        pq = []

        for num in nums:
            counts[num] += 1
            heappush(pq, (-counts[num], num))

        ret = set()
        while len(ret) < k:
            ret.add(heappop(pq)[1])
        
        return list(ret)

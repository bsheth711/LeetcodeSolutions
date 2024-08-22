class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)

        for num in nums:
            counts[num] += 1

        return nlargest(k, counts, key=lambda num: counts[num])
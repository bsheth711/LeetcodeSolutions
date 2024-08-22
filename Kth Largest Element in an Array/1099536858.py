class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:

            if len(pq) < k:
                heappush(pq, num)
            else:
                heappushpop(pq, num)
        
        return min(pq)
        
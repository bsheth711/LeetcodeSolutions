class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        total = 0
        idx = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                idx = i + 1
        
        return -1 if (total < 0) else idx
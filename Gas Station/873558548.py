class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tank = 0
        totalGas = 0
        totalCost = 0
        idx = 0

        # find best opportunity
        for i, (g, c) in enumerate(zip(gas, cost)): 
            tank += g - c

            totalGas += g
            totalCost += c

            if tank < 0:
                tank = 0
                idx = i + 1

        if totalGas < totalCost:
            return -1

        return idx

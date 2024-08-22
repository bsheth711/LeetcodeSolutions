class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        num = 0

        costs.sort()

        for c in costs:
            if total + c <= coins:
                total += c
                num += 1

        return num 
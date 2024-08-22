class Solution:
    def minimumPushes(self, word: str) -> int: 
        counts = Counter(word)
        curCount = 0
        total = 0
        
        for c, count in counts.most_common():
            mult = (curCount // 8) + 1
            total += count * mult
            curCount += 1

        return total
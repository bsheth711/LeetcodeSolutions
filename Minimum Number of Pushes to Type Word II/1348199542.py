class Solution:
    def minimumPushes(self, word: str) -> int: 
        counts = Counter(word)
        #counts.most_common()
        curCount = 0
        total = 0
        print(counts)
        
        for c, count in counts.most_common():

            mult = (curCount // 8) + 1
            print(f"c: {c}, curCount: {curCount}, count: {count}, mult: {mult} additional: {count*mult}")
            total += count * mult
            curCount += 1

        return total
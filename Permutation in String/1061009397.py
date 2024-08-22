class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(lambda: 0)

        for c in s1:
            counts[c] += 1


        i = 0
        j = 0
        
        backup = counts.copy()
        while j < len(s2):
            #print(counts)
            c = s2[j]

            if c in counts:
                counts[c] -= 1

                if counts[c] == 0:
                    del counts[c]
                
                if not counts:
                    return True 

            else:
                if s2[i] in backup:
                    counts[s2[i]] += 1 
                    j -= 1
                i += 1

            
            j += 1


        return False
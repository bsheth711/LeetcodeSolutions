class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        idx = 0
        hashmap = {}
        values = set()

        if len(words) != len(pattern):
            return False

        for word in words:
            if hashmap.get(pattern[idx]) == None:
                hashmap[pattern[idx]] = word

                if word in values:
                    return False
                else:
                    values.add(word)
                    
            elif hashmap[pattern[idx]] != word:
                return False
            
            idx += 1

        

        
        return True

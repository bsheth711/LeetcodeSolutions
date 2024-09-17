class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        
        lowerCaseStart = 97

        firstIsCapital = True if ord(word[0]) < lowerCaseStart else False
        secondIsCapital = True if ord(word[1]) < lowerCaseStart else False

        if not firstIsCapital and secondIsCapital:
            return False

        allShouldBeCapital = firstIsCapital and secondIsCapital

        for i, c in enumerate(word[2:]):
            cur = ord(c)

            if allShouldBeCapital and cur >= lowerCaseStart:
                return False
            
            if not allShouldBeCapital and cur < lowerCaseStart:
                return False 

        return True
        
        
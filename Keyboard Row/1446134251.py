class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        ret = []

        for word in words:
            if self.canType(word, row1) or self.canType(word, row2) or self.canType(word, row3):
                ret.append(word)
 
        return ret
    
    def canType(self, word, letters):

        for char in word.lower():
            if char not in letters:
                return False
        
        return True


        
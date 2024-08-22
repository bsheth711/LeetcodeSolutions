class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if len(digits) == 0:
            return res

        mapping = {'2':['a', 'b', 'c'], 
            '3':['d', 'e', 'f'], 
            '4':['g', 'h', 'i'], 
            '5':['j', 'k', 'l'], 
            '6':['m', 'n', 'o'], 
            '7':['p', 'q', 'r', 's'], 
            '8':['t', 'u', 'v'], 
            '9':['w', 'x', 'y', 'z']}
    
        def dfs(cur, i):
            if len(cur) == len(digits): 
                res.append(''.join(cur))
                return
            
            for letter in mapping[digits[i]]:
                cur.append(letter)
                dfs(cur, i + 1)
                cur.pop()
        
        dfs([], 0)

        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        idx = 0

        while True:
            if idx >= len(strs[0]):
                return prefix
            possible = strs[0][idx]

            for string in strs:  
                if idx >= len(string):
                    return prefix
                
                if possible != string[idx]:
                    return prefix
                
            prefix += possible
            idx += 1
                



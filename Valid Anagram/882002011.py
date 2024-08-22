class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basically check if two strings have the exact same characters, no matter what order they are in
        # they need to have the same number of each character too

        sHash = {}
        tHash = {}

        for char in s:
            if char in sHash:
                sHash[char] += 1
            else:
                sHash[char] = 1
        
        for char in t:
            if char in tHash:
                tHash[char] += 1
            else:
                tHash[char] = 1
        
        return tHash == sHash

        
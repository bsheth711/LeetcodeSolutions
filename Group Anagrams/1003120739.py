class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[self.customHash(s)].append(s)
        
        ret = []
        for group in groups:
            ret.append(groups[group])
        
        return ret


    def customHash(self, string: str) -> int:
        total = 0
        primes = [709, 5381, 52711, 167449, 648391, 1128889, 2269733, 3042161, 4535189, 7474967, 9737333, 14161729, 17624813, 19734581, 23391799, 29499439, 37139213, 38790341, 50728129, 56011909, 59053067, 68425619, 77557187, 87019979, 101146501, 113256643, 119535373]

        for c in string:
            total += primes[ord(c) - ord('a')]
        
        return total

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        weights = {}
        for i in range(len(order)):
            weights[order[i]] = i

        def compare(str1, str2):
            for a, b in itertools.zip_longest(str1, str2):
                if not a:
                    return -1

                if not b:
                    return 1
                 
                if weights[a] < weights[b]:
                    return -1
                elif weights[a] > weights[b]: 
                    return 1
                 
            return 0

        return words == sorted(words, key=cmp_to_key(compare))

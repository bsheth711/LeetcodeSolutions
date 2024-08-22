class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)

        for string in arr:
            counts[string] += 1
        
        counter = 0
        for string in counts:
            if counts[string] == 1:
                counter += 1

                if counter == k:
                    return string
        
        return ""
        
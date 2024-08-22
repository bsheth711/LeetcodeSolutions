class TimeMap:

    def __init__(self):
        self.groups = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heappush(self.groups[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.groups[key]
        l = 0
        r = len(ls) - 1
        possible = []

        while l <= r:
            mid = (l + r) // 2

            if ls[mid][0] <= timestamp:
                possible.append(ls[mid])
                l = mid + 1
            else:
                r = mid - 1
        
        if not possible:
            return ""

        return possible[-1][1]



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
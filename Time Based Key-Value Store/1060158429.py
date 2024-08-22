class TimeMap:

    def __init__(self):
        self.groups = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.groups[key].append((timestamp, value))
        #heappush(self.groups[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.groups[key]
        l = 0
        r = len(ls) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if ls[mid][0] <= timestamp:
                res = ls[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
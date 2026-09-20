class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys or key not in self.keys:
            return ""
        n = len(self.keys[key])
        l,r = 0, n-1
        while l <= r:
            m = l + (r-l) // 2
            midt = self.keys[key][m][1]
            if midt == timestamp:
                return self.keys[key][m][0]
            elif midt < timestamp:
                l = m + 1
            else:
                r = m -1
        return self.keys[key][r][0]

        

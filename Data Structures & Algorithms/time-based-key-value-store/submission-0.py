class TimeMap:

    def __init__(self):
        self.storage = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ''
        values = self.storage[key]
        if timestamp < values[0][1]:
            return ''
        
        l = 0
        r = len(values)
        while r-l > 1:
            m = (l + r) // 2
            if timestamp < values[m][1]:
                r = m
            else:
                l = m
        
        return values[l][0]
        

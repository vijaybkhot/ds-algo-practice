class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or not self.time_map[key]:
            return ""

        val_list= self.time_map[key]
        if val_list[0][1] > timestamp:
            return ""
        left, right = 0, len(val_list)-1
        while left <= right:
            mid = (left+right) // 2
            curr_timestamp = val_list[mid][1]
            if curr_timestamp == timestamp:
                return val_list[mid][0]
            elif curr_timestamp < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return val_list[right][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
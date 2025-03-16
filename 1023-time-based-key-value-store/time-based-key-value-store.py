class TimeMap(object):

    def __init__(self):
        self.map = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key] = self.map.get(key, [])
        self.map[key].append([timestamp, value])        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.map or self.map[key][0][0] > timestamp:
            return ""
        
        value_arr = self.map[key]
        left, right = 0, len(value_arr)-1
        while left <= right:
            mid = (left + right) // 2
            if value_arr[mid][0] < timestamp:
                left = mid + 1
            elif value_arr[mid][0] > timestamp:
                right = mid - 1
            else:
                return value_arr[mid][1]

        return value_arr[right][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
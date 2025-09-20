class Router:

    def __init__(self, memoryLimit: int):
        self.size = 0
        self.memoryLimit = memoryLimit
        self.time_queue = deque([])
        self.time_set = defaultdict(set)
        self.destination_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if timestamp in self.time_set and (source, destination) in self.time_set[timestamp]:
            return False
        elif self.size == self.memoryLimit:
            # Remove the oldest packer
            self.removeOldest()

        self.time_set[timestamp].add((source, destination))
        self.size += 1
        self.time_queue.append((source, destination, timestamp))
        self.destination_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.size == 0:
            return []
        return self.removeOldest()
    
    def removeOldest(self) -> List[int]:
        source, destination, oldest_time = self.time_queue.popleft()
        self.time_set[oldest_time].remove((source, destination))
        self.destination_map[destination].pop(0)
        self.size -= 1
        return [source, destination, oldest_time]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = 0
        # for i in range(startTime, endTime+1):
        #     if i in self.time_set:
        #         for s, d in self.time_set[i]:
        #             if d == destination:
        #                 packets += 1
        # for source, timestamp in self.destination_map[destination]:
        #     if startTime <= timestamp <= endTime:
        #         packets += 1  
        destinations = self.destination_map[destination]
        startIndex = bisect_left(destinations, startTime)
        endIndex = bisect_right(destinations, endTime)
        return endIndex-startIndex


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
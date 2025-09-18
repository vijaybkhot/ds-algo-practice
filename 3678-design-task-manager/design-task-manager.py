class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_heap = [(-priority, -taskId, userId) for userId, taskId, priority in tasks]
        heapq.heapify(self.task_heap)

        self.task_priority_map = { taskId:(priority, userId) for userId, taskId, priority in tasks}

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_priority_map[taskId] = (priority, userId)
        heapq.heappush(self.task_heap, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        _, userId = self.task_priority_map[taskId]
        self.task_priority_map[taskId] = (newPriority, userId)
        heapq.heappush(self.task_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_priority_map:
            del self.task_priority_map[taskId]
        

    def execTop(self) -> int:
        while self.task_heap:
            priority, taskId, userId = heapq.heappop(self.task_heap)
            taskId *= -1
            priority *= -1
            if taskId not in self.task_priority_map or self.task_priority_map[taskId][0] != priority or self.task_priority_map[taskId][1] != userId:
                continue
            else:
                self.rmv(taskId)
                return userId

        return -1 
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # # First Attempt:
        # curr_index = 0
        # dq = deque(tasks)
        # startTime, duration = dq[0]
        # finishTime = startTime + duration
        # currTime = startTime
        # availableTasks = []
        # currentTask = []
        # res = []

        # while dq or availableTasks:
        #     while  dq and dq[0][0] == currTime:
        #         curr_task = dq.popleft()
        #         heapq.heappush(availableTasks, (curr_task[1], curr_index, curr_task))
        #         curr_index += 1
        #     if currTime >= finishTime and currentTask:
        #         currentTask.pop()
        #     if not currentTask and availableTasks:
        #         taskToAdd = heapq.heappop(availableTasks)
        #         currentTask.append(taskToAdd[2])
        #         res.append(taskToAdd[1])
        #         startTime, duration = currentTask[0]
        #         finishTime = startTime + duration
        #     currTime += 1

        # return res

        #More readable approach
        indexed_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(min_heap, (process, idx))
                i += 1
            
            # If no task is available, jump time to the next task's enqueue time
            if not min_heap:
                time = indexed_tasks[i][0]
                continue
            
            # Process the next task
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            result.append(idx)

        return result



        
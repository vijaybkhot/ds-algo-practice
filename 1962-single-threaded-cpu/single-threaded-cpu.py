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

        # #More readable approach
        # indexed_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        # result = []
        # min_heap = []
        # time = 0
        # i = 0
        # n = len(tasks)

        # while i < n or min_heap:
        #     while i < n and indexed_tasks[i][0] <= time:
        #         enqueue, process, idx = indexed_tasks[i]
        #         heapq.heappush(min_heap, (process, idx))
        #         i += 1
            
        #     # If no task is available, jump time to the next task's enqueue time
        #     if not min_heap:
        #         time = indexed_tasks[i][0]
        #         continue
            
        #     # Process the next task
        #     proc_time, idx = heapq.heappop(min_heap)
        #     time += proc_time
        #     result.append(idx)

        # return result




        task_heap = [(enq,idx, proc) for idx, [enq, proc] in enumerate(tasks)]
        task_heap.sort(reverse=True)
        time = task_heap[-1][0]
        res = []
        available_tasks = []
    
        while task_heap or available_tasks:
            if not available_tasks and time < task_heap[-1][0]:
                time = task_heap[-1][0]
            while task_heap and task_heap[-1][0] <= time:
                enq, idx, proc = task_heap.pop()
                heapq.heappush(available_tasks, (proc, idx))
            proc, idx = heapq.heappop(available_tasks)
            res.append(idx)
            time += proc
        
        return res













        
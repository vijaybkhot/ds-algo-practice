class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers = [(weight, idx, 0) for idx, weight in enumerate(servers)]
        heapq.heapify(servers)
        i = 0
        no_of_tasks = len(tasks)
        ans = []
        time = 0
        servers_in_use = []

        while i < no_of_tasks:
            time = max(time, i)
            
            if not servers and servers_in_use:
                time = servers_in_use[0][0]

            while servers_in_use and servers_in_use[0][0] <= time:
                curr_task_completion_time, weight, idx = heapq.heappop(servers_in_use)
                heapq.heappush(servers, (weight, idx, curr_task_completion_time))


            curr_task_time = tasks[i]
            weight, idx, completion_time = heapq.heappop(servers)
            curr_task_completion_time = time + curr_task_time
            ans.append(idx)
            heapq.heappush(servers_in_use, (curr_task_completion_time, weight, idx))
            i += 1
            
            
        return ans
                
            

        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # interval_count = 0
        # freq_map = defaultdict(int)
        # for task in tasks:
        #     freq_map[task] += 1
        
        # q =deque([])
        # for key in freq_map:
        #     q.append([key, freq_map[key], None])
        # while q:
        #     key, count, next_interval = q.popleft()
        #     if next_interval is not None and next_interval > interval_count:
        #         interval_count = next_interval

        #     interval_count += 1
        #     count -= 1
        #     if count > 0:
        #         q.append([key, count, interval_count + n])
        
        # return interval_count

        # Using heap data structure
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        heap = []
        for task in freq_map:
            heapq.heappush(heap, (-freq_map[task], task))
        total_interval = 0
        while heap:
            task_stack = []
            i = 0
            last_iteration = False
            if heap[0][0] == -1:
                last_iteration = True
            if not last_iteration:
                while i <= n:
                    if heap:
                        task_stack.append(heapq.heappop(heap))
                    i += 1
                    total_interval += 1
            else:
                while heap:
                    heapq.heappop(heap)
                    total_interval += 1
            while task_stack:
                freq, task = task_stack.pop()
                freq += 1
                if freq < 0:
                    heapq.heappush(heap, (freq, task))
        
        return total_interval


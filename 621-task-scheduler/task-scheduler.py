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

        # # Using heap data structure
        # freq_map = defaultdict(int)
        # for task in tasks:
        #     freq_map[task] += 1
        # heap = []
        # for task in freq_map:
        #     heapq.heappush(heap, (-freq_map[task], task))
            
        # total_interval = 0
        # while heap:
        #     task_stack = []
        #     i = 0
        #     last_iteration = False
        #     if heap[0][0] == -1:
        #         last_iteration = True
        #     if not last_iteration:
        #         while i <= n:
        #             if heap:
        #                 task_stack.append(heapq.heappop(heap))
        #             i += 1
        #             total_interval += 1
        #     else:
        #         while heap:
        #             heapq.heappop(heap)
        #             total_interval += 1
        #     while task_stack:
        #         freq, task = task_stack.pop()
        #         freq += 1
        #         if freq < 0:
        #             heapq.heappush(heap, (freq, task))

        # return total_interval

        # # More readable solution:
        # freq_map = Counter(tasks)
        # max_heap = [-freq for freq in freq_map.values()]
        # heapq.heapify(max_heap)

        # total_time = 0

        # while max_heap:
        #     temp = []
        #     for i in range(n+1):
        #         if max_heap:
        #             freq = heapq.heappop(max_heap)
        #             if freq + 1 < 0:
        #                 temp.append(freq + 1)
        #         total_time += 1
        #         if not max_heap and not temp:
        #             break
        #     for freq in temp:
        #         heapq.heappush(max_heap, freq)
        
        # return total_time

        # # Simulation using heap
        # freq_dict = defaultdict(int)
        # for char in tasks:
        #     freq_dict[char]+=1

        # pq = [(-freq_dict[char], 0, char) for char in freq_dict]
        # heapq.heapify(pq)
        
        # curr_time = 0
        # while pq:
        #     curr_tasks = []
        #     for i in range(n+1):
        #         if pq:
        #             if pq[0][1] > curr_time:
        #                 curr_time = pq[0][1]
        #             freq, task_start, char = heapq.heappop(pq)
        #             if freq < -1:
        #                 heapq.heappush(curr_tasks, (freq+1, curr_time+n+1, char))
        #             curr_time += 1
        #     if curr_tasks:
        #         for task in curr_tasks:
        #             heapq.heappush(pq, task)

        # return curr_time

        # # Mathematical solution:
        # freq = list(Counter(tasks).values())
        # max_freq = max(freq)
        # max_count = freq.count(max_freq)

        # return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

        # More optimized heap approach:
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        cooldown = deque()  # (time when task is ready, frequency)
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # decrement freq
                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                ready_time, ready_cnt = cooldown.popleft()
                heapq.heappush(max_heap, ready_cnt)

        return time




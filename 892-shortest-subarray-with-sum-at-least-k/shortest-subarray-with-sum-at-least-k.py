class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        # mono_q = deque()
        # prefix_sums = [0]
        # res = len(nums) + 1

        # for num in nums:
        #     prefix_sums.append(prefix_sums[-1] + num)


        # for i, prefix in enumerate(prefix_sums):
            
        #     while mono_q and prefix - prefix_sums[mono_q[0]] >= k:
        #         res = min(res, i - mono_q.popleft())

        #     while mono_q and prefix_sums[mono_q[-1]] >= prefix:
        #         mono_q.pop()
            
        #     mono_q.append(i)

        res = len(nums)+1
        min_heap = []   #(prefix_sum, idx)
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= k:
                res = min(res, r+1)  
            while min_heap and curr_sum - min_heap[0][0] >= k:
                prefix, end_idx = heapq.heappop(min_heap)
                res = min(res, r - end_idx)     
            heapq.heappush(min_heap, (curr_sum ,r)) 
        return res if res <= len(nums) else -1
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # n = len(nums)//3
        # first_heap = []
        # second_heap = []
        
        # for i in range(len(nums)//2+1):
        #     heapq.heappush(first_heap, -nums[i])
        #     if i+(len(nums)//2) < len(nums):
        #         heapq.heappush(second_heap, nums[i+(len(nums)//2)])
        
        

        # while len(first_heap) > n or len(second_heap)>n:
        #     if len(second_heap) > len(first_heap):
        #         heapq.heappop(second_heap)
        #     else:
        #         if len(first_heap) > n:
        #             heapq.heappop(first_heap)
        
        
        # first_sum, second_sum = 0, sum(second_heap)
        
        # while first_heap:
        #     element = -heapq.heappop(first_heap)
        #     first_sum += element
        
        # return first_sum-second_sum


        n = len(nums) // 3
        
        # prefix: max heap to keep smallest n elements from the first 2n elements
        left_sum = sum(nums[:n])
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        left_sums = [left_sum]
        
        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)
            left_sums.append(left_sum)
        
        # suffix: min heap to keep largest n elements from the last 2n elements
        right_sum = sum(nums[2 * n:])
        min_heap = nums[2 * n:]
        heapq.heapify(min_heap)
        right_sums = [0] * (n + 1)
        right_sums[n] = right_sum
        
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)
            right_sums[i - n] = right_sum
        
        # Find the minimum difference
        result = float('inf')
        for i in range(n + 1):
            result = min(result, left_sums[i] - right_sums[i])
        
        return result

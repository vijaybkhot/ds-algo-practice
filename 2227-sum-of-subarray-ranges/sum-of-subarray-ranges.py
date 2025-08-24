class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def greater(arr):
            prev_greater = [0]*len(arr)
            next_greater = [0]*len(arr)
            stack = []
            for idx, num in enumerate(arr):
                while stack and stack[-1][0] <= num:
                    _, i = stack.pop()
                    next_greater[i] = idx - i
                
                last_idx = stack[-1][1] if stack else -1
                prev_greater[idx] = idx - last_idx
                stack.append((num, idx))
            
            for _, idx in stack:
                if next_greater[idx] == 0:   # only set if not found
                    next_greater[idx] = len(arr) - idx
            
            return prev_greater, next_greater
        
        def smaller(arr):
            prev_smaller = [0]*len(arr)
            next_smaller = [0]*len(arr)
            stack = []
            for idx, num in enumerate(arr):
                while stack and stack[-1][0] >= num:
                    _, i = stack.pop()
                    next_smaller[i] = idx - i

                last_idx = stack[-1][1] if stack else -1
                prev_smaller[idx] = idx - last_idx
                stack.append((num, idx))
            for num, idx in stack:
                if next_smaller[idx] == 0:
                    next_smaller[idx] = len(arr) - idx
            
            return prev_smaller, next_smaller
        
        prev_smaller, next_smaller = smaller(nums)
        prev_greater, next_greater = greater(nums)
        max_total = 0
        min_total = 0

        for i in range(len(nums)):
            max_total = (max_total + prev_greater[i]*next_greater[i]*nums[i]) 
            min_total = (min_total + prev_smaller[i]*next_smaller[i]*nums[i])
        return max_total - min_total




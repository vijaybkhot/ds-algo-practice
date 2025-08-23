class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10**9)+7
        
        # Next smallest
        def get_next_smallest(arr):
            next_smallest = [0]*len(arr)
            stack = []
            for i, num in enumerate(arr):
                while stack and stack[-1][0] > num:
                    _, idx = stack.pop()
                    next_smallest[idx] = (i - idx)
                stack.append((num, i))
            if stack:
                last_idx = stack[-1][1]

                for num, idx in stack:
                    next_smallest[idx] = last_idx-idx+1

            return next_smallest
        # Get Prev smallest elements
        def get_prev_smallest(arr):
            prev_smallest = [0]*len(arr)
            stack = []
            for idx, num in enumerate(arr):
                while stack and stack[-1][0] > num:
                    _, i = stack.pop()
                
                if stack:
                    start_idx = stack[-1][1]
                    prev_smallest[idx] = idx - start_idx
                else:
                    prev_smallest[idx] = idx + 1
                stack.append((num, idx))
            
            return prev_smallest
        
        prev_smallest = get_prev_smallest(arr)
        next_smallest = get_next_smallest(arr)
        total = 0
        for i in range(len(arr)):
            total = (total + arr[i]*prev_smallest[i]*next_smallest[i]) % MOD
        
        return total
                
                
                
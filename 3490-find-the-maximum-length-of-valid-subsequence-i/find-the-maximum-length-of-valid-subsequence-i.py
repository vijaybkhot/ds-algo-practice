class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = {}
        # def dfs(i, mod_value):
        #     if (i, mod_value) in dp:
        #         return dp[(i, mod_value)]
        #     if i >= n:
        #         return 0
            
        #     sub_len = 0
        #     for j in range(i+1, n):
        #         if (nums[i]+nums[j]) % 2 == mod_value:
        #             sub_len = max(sub_len, 1 + dfs(j, mod_value))
                
            
        #     dp[(i, mod_value)] = sub_len
        #     return sub_len
        
        # max_len = 0
        # for i in range(n):
        #     max_len = max(max_len, 1 + dfs(i, 0))
        #     max_len = max(max_len, 1 + dfs(i, 1))
        
        # return max_len

        # n = len(nums)
        # dp_even = [1] * n
        # dp_odd = [1] * n

        # for i in range(n):
        #     for j in range(i):
        #         if (nums[j] + nums[i]) % 2 == 0:
        #             dp_even[i] = max(dp_even[i], dp_even[j] + 1)
        #         else:
        #             dp_odd[i] = max(dp_odd[i], dp_odd[j] + 1)
        
        # return max(max(dp_even), max(dp_odd))

        # All Even, all_odd, even_odd, odd_even
        # Alternate even odd
        def get_alternate_even_odd_len(isEven):
            sub_len = 0
            for i in range(n):
                if isEven:
                    if nums[i]%2:
                        sub_len += 1
                        isEven = not isEven
                else:
                    if not nums[i]%2:
                        sub_len += 1
                        isEven = not isEven
            return sub_len
    
        all_even = 0
        all_odd = 0
        for num in nums:
            if num%2:
                all_even += 1
            else:
                all_odd += 1
        
        
        even_odd = get_alternate_even_odd_len(isEven=True)
        odd_even = get_alternate_even_odd_len(isEven=False)
        
        
        return max(all_even, all_odd, even_odd, odd_even)



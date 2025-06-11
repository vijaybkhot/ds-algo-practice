class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]  # Add virtual balloons
        n = len(nums)
        memo = {}

        def dfs(left, right):
            if left + 1 == right:  # no balloon to burst between
                return 0
            if (left, right) in memo:
                return memo[(left, right)]

            max_coins = 0
            for i in range(left + 1, right):  # pick i as last to burst
                coins = nums[left] * nums[i] * nums[right]
                coins += dfs(left, i) + dfs(i, right)
                max_coins = max(max_coins, coins)

            memo[(left, right)] = max_coins
            return max_coins

        return dfs(0, n - 1)
        
        

        # # Recursive Solution:
        # def dfs(arr):
        #     if len(arr) == 0:
        #         return 0
        #     max_coins = 0
        #     for j in range(len(arr)):
        #         left = arr[j-1] if j-1 >= 0 else 1
        #         right = arr[j+1] if j+1 < len(arr) else 1
        #         curr_product = arr[j]*left*right
        #         max_coins = max(max_coins, curr_product + dfs(arr[:j]+arr[j+1:]))
        #     return max_coins
            
        # return dfs(nums)

        # Top - Down DP - Solution:
        # dp = {}
        # def dfs(arr_str):
        #     if len(arr_str) == 0:
        #         return 0
        #     if arr_str in dp:
        #         return dp[arr_str]
        #     arr_s = arr_str.split(',')
        #     arr = [int(str_num) for str_num in arr_s]
            
        #     max_coins = 0
        #     for j in range(len(arr)):
        #         left = arr[j-1] if j-1 >= 0 else 1
        #         right = arr[j+1] if j+1 < len(arr) else 1
        #         curr_product = arr[j]*left*right
        #         new_arr = arr[:j]+arr[j+1:]
        #         new_arr_str = ','.join(str(num) for num in new_arr)
                
        #         max_coins = max(max_coins, curr_product + dfs(new_arr_str))
        #     dp[arr_str] = max_coins
        #     return max_coins
        
        # arr_str = ','.join(str(num) for num in nums)
        # return dfs(arr_str)
        
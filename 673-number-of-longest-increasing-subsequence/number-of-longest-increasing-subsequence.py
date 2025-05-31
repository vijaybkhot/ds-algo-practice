class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # # Using binary search DP - Incorrect for counting LIS
        # dp = []
        # dp.append(nums[0])
        # res = 1

        # for i in range(1, len(nums)):
        #     if dp[-1] < nums[i]:
        #         dp.append(nums[i])
        #         continue
        #     l, r = 0, len(dp)-1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if dp[mid] < nums[i]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     idx = l
        #     dp[l] = nums[i]
        #     res += 1
        
        # return res

        # Using DP based solution
        n = len(nums)
        if n == 0:
            return 0
        length = [1] * n
        count = [1] * n
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        LIS = max(length)
        
        return sum(c for l, c in zip(length, count) if l == LIS)
        
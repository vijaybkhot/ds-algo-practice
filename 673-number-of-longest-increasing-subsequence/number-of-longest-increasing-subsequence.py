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

        # # Using DP based solution
        # n = len(nums)
        # if n == 0:
        #     return 0
        # length = [1] * n
        # count = [1] * n
        
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if length[j] + 1 > length[i]:
        #                 length[i] = length[j] + 1
        #                 count[i] = count[j]
        #             elif length[j] + 1 == length[i]:
        #                 count[i] += count[j]
        
        # LIS = max(length)
        
        # return sum(c for l, c in zip(length, count) if l == LIS)
        # # Inefficient DFS appraoch
        # n = len(nums)
        # @lru_cache(None)
        # def length(i, prev_index):
        #     if i == n:
        #         return 0
        #     taken = 0
        #     if prev_index == -1 or nums[i] > nums[prev_index]:
        #         taken = 1 + length(i+1, i)
        #     not_taken = length(i+1, prev_index)
        #     return max(taken, not_taken)

        # LIS_len = length(0, -1)

        # @lru_cache(None)
        # def count(i, prev_index, curr_len):
        #     if i == n:
        #         return 1 if curr_len == LIS_len else 0
        #     total = 0
        #     if prev_index == -1 or nums[i] > nums[prev_index]:
        #         total += count(i+1, i, curr_len + 1)
        #     total += count(i+1, prev_index, curr_len)
        #     return total

        # return count(0, -1, 0)

        n = len(nums)
        length = [1]*n
        count = [1]*n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    if length[j]+1 > length[i]:
                        length[i] = length[j]+1
                        count[i] = count[j]
                    elif length[j]+1 == length[i]:
                        count[i] += count[j]
        
        LIS = max(length)

        return sum(c for c, l in zip(count, length) if l == LIS)

            
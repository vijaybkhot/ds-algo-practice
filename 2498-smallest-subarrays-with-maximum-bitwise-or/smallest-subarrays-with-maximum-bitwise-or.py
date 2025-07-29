class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        # # Brute Force: TLE
        # n = len(nums)
        # maxOr = 0
        # for num in nums:
        #     maxOr = maxOr | num
        
        # maxOrDp = [0]*n
        # maxOrDp[n-1] = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     maxOrDp[i] = max(nums[i], nums[i]|maxOrDp[i+1])
        
        # res = [1]*n

        # for i in range(n-2, -1, -1):
        #     currOr = nums[i]
        #     for j in range(i, n):
        #         currOr = currOr | nums[j]
        #         if currOr == maxOrDp[i]:
        #             res[i] = j-i+1
        #             break
        
        # return res
        n = len(nums)
        res = [1]*n

        for i in range(n):
            curr = nums[i]
            prev = i-1
            while prev >= 0 and (nums[prev] | curr) != nums[prev]:
                res[prev] = i-prev+1
                nums[prev] |= curr
                prev -= 1
        
        return res

        n = len(nums)
        pos = [-1] * 31
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            j = i
            for bit in range(31):
                if (nums[i] & (1 << bit)) == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                else:
                    pos[bit] = i
            ans[i] = j - i + 1
        return ans
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        def find_index_less_than_equal(num, nums):
            l, r = 0, len(nums)-1
            res = l
            while l <= r:
                mid = (l+r) // 2
        
                if nums[mid] <= num:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        nums.sort()
        right = len(nums)-1
        mod = 10**9+7
        res = 0
        for left in range(len(nums)):
            while nums[left] +nums[right] > target and left <= right:
                right -= 1
            if left <= right:
                res += (2**(right-left))
                res %= mod
        
        return res

            
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        if k == 1 or len(nums) == 1:
            return sum(nums)
        if k >= len(nums):
            return max(nums)

        n = len(nums)
        prefix_arr = [nums[0]] * n
        for i in range(1, n):
            prefix_arr[i] = nums[i] + prefix_arr[i-1]

        def can_split(nums, k, max_sum):
            count = 1  # at least one subarray
            current_sum = 0
            for num in nums:
                if num > max_sum:
                    return False  # single element is too big
                if current_sum + num <= max_sum:
                    current_sum += num
                else:
                    count += 1
                    current_sum = num

            return count <= k

        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left+right) // 2
            if can_split(nums, k, mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res


            
        
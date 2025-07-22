class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr_set = set()
        curr_sum, max_sum = 0, 0
        res_left, res_right = 0, 0

        left = 0
        for right in range(len(nums)):
            if nums[right] not in curr_set:
                curr_sum += nums[right]
                curr_set.add(nums[right])
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res_left = left
                    res_right = right
            else:
                while left < right and nums[right] in curr_set:
                    curr_set.remove(nums[left])
                    curr_sum -= nums[left]
                    left += 1
                curr_sum += nums[right]
                curr_set.add(nums[right])
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    res_left = left
                    res_right = right
                
        
        return max_sum


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            curr_num = nums[i]
            curr_target = -curr_num
            left, right = i + 1, n-1
            curr_triplet = []
            while left < right:
                if nums[left] + nums[right] == curr_target:
                    curr_triplet = [nums[i], nums[left], nums[right]]
                    if curr_triplet in res:
                        curr_triplet = []
                    if len(curr_triplet) == 3:
                        res.append(curr_triplet)
                    left += 1
                    right -= 1 
                elif nums[left] + nums[right] < curr_target:
                    left += 1
                else:
                    right -= 1
        
        return res

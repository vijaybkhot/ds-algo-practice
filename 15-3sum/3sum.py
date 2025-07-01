class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        i = 0
        while i < (len(nums)-2):
            j, k = i+1, len(nums)-1
            curr_num = nums[i]
            while j < k:
                if curr_num + nums[j] + nums[k] == 0:
                    res.append([curr_num, nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                elif curr_num + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            
            while i < len(nums)-2 and nums[i+1] == nums[i]:
                i += 1
            i += 1
            
        return res
        
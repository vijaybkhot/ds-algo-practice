class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            num_i = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            target = 0 - num_i
            while j < k:
                num_j, num_k = nums[j], nums[k]
                curr_sum = num_j + num_k
                if curr_sum == target:
                    res.append([num_i, num_j, num_k])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif curr_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return res


        
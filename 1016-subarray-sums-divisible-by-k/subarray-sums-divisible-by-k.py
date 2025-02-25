class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # edge cases
        if not nums:
            return 0
        if len(nums)== 1:
            if nums[0] % k != 0:
                return 0
            else:
                return 1
        
        res = 0
        # Remainder frequency hash map
        remainder = {}
        prefix = 0
        for index, num in enumerate(nums, start=0):
            prefix += num
            curr_remainder = prefix % k
            remainder.setdefault(curr_remainder, []).append(index)
            res += len(remainder[curr_remainder]) - 1 if curr_remainder !=0 else len(remainder[curr_remainder])
                    
        return res
        
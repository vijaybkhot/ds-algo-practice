class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # res = []
        # if not nums:
        #     return []
        # prev, start, end, = nums[0], nums[0], None
       
        # i = 1
        # while i < len(nums):
        #     while i < len(nums) and nums[i] == prev+1:
        #         prev = nums[i]
        #         end = nums[i]
        #         i += 1
        #     if end is not None:
        #         res.append(str(start) + "->" + str(end))
        #     else:
        #         res.append(str(start))
        #     if i < len(nums):
        #         start = nums[i]
        #         end = None
        #         prev = start
        #         if i+1 == len(nums):
        #             res.append(str(start))
        #     i += 1
        # if not res:
        #     res.append(str(start))
        
        # return res

        res = []
        i = 0
        while i < len(nums):
            start, prev = nums[i], nums[i]
            end = start
            while i < len(nums)-1 and nums[i+1] == prev+1:
                prev = nums[i+1]
                end = prev
                i += 1
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            i += 1
        return res
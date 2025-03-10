class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n) solution
        result = []
        for i in range(len(nums)):
            if nums[i] == target and len(result)== 0:
                result.append(i)
            elif nums[i] == target and len(result)>= 1:
                if(len(result)==1):
                    result.append(i)
                else:
                    result[1] = i
        
        if len(result)== 1:
            if nums[-1] == target:
                result.append(len(nums)-1)
            else:
                result.append(result[0])
        if len(result)==0:
            result = [-1, -1]
        
        return result


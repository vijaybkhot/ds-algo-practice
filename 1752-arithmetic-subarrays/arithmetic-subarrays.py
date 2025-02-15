class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        # Brute force solution
        result = []
        for i in range(len(l)):
            curr_list = nums[l[i]:r[i]+1]
            curr_list.sort()
            curr_bool = True
            for i in range(2, len(curr_list)):
                if curr_list[i]-curr_list[i-1] != curr_list[1] - curr_list[0]:
                    curr_bool = False
                    break
            result.append(curr_bool)
        return result
                


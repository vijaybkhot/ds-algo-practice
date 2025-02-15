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
            left_index = l[i]
            right_index = r[i]+1
            curr_list = nums[left_index:right_index]
            curr_list.sort()
            initial_difference = curr_list[1] - curr_list[0]
            curr_bool = True
            for i in range(2, len(curr_list)):
                if curr_list[i]-curr_list[i-1] != initial_difference:
                    curr_bool = False
                    break
            result.append(curr_bool)
        return result
                


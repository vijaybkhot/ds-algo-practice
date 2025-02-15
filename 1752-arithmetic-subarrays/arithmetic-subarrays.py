class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        # Brute force solution
        # result = []
        # for i in range(len(l)):
        #     curr_list = nums[l[i]:r[i]+1]
        #     curr_list.sort()
        #     curr_bool = True
        #     for i in range(2, len(curr_list)):
        #         if curr_list[i]-curr_list[i-1] != curr_list[1] - curr_list[0]:
        #             curr_bool = False
        #             break
        #     result.append(curr_bool)
        # return result
        
        # Form a hash set

        result = [True for i in range(len(l))]

        # Loop over each subarray to check for duplicates
        for i in range(len(l)):
            if (r[i] - l[i] + 1) <= 1:
                continue
            curr_list = nums[l[i]:r[i]+1]
             # Find the min and max elements in the current list
            min_element = min(curr_list)
            max_element = max(curr_list)

            if (min_element == max_element):
                continue

            curr_set = set(curr_list)
            # Check for duplicates
            if len(curr_set) != len(curr_list):
                result[i] = False
                continue  # Skip further checks if duplicates are found
            
            # Calculate the expected difference
            expected_difference = (max_element - min_element) / (len(curr_list) - 1)
            
            # If the expected difference is not an integer, it's not an arithmetic progression
            if expected_difference != int(expected_difference):
                result[i] = False
                continue
            
            # Check if all elements in the arithmetic progression exist
            for j in range(len(curr_list)):
                if (min_element + (expected_difference * j)) not in curr_set:
                    result[i] = False
                    break
        return result
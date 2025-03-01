class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Brute force solution:
        # max_num = max(nums)
        # for num in range(1, max_num):
        #     if num not in nums:
        #         return num
        
        # return max_num + 1

        # # 2nd Brute force solution
        # range_num = len(nums)
        # for i in range(1, range_num+2):
        #     if i not in nums:
        #         return i
        # return range_num + 2

        # # Using hash set - But the space complexity is O(n). Time complexity is O(n)
        # nums_set = set(nums)
        # for i in range(1, len(nums_set)+1):
        #     if i not in nums_set:
        #         return i
        
        # return len(nums_set) + 1

        # Optimal O(n) time and O(1) space complexity solution
        # Replace negative numbers with 0
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        # Loop over each number, and mark the index of that number negative. i.e. if 1 is present, make the number at index 0 negative
        # If a number is out of bounds of the array, skip it
        for i in range(n):      
            num = abs(nums[i])
            if 1 <= num <= n:
                # Mark the index corresponding to the number as negative
                if nums[num-1] > 0:
                    nums[num-1] = - nums[num-1]
                elif nums[num-1] == 0:
                    nums[num-1] = -1 * (n+1)
        
        # Now loop over the transformed array and the first index whose vlaue is positive is the answer
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                return i
        
        return n + 1
        


                

        
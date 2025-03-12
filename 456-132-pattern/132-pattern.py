class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # # Brute force solution
        # stack = []
        
        # for num in nums:
        #     if len(stack) >= 2:
        #         pattern = ""
        #         backup = []
        #         # We have 2 in hand. First find a 3
        #         while stack and stack[-1] <= num:
        #             backup.append(stack.pop())
        #         if stack and stack[-1] > num:
        #             pattern = "12"
        #             backup.append(stack.pop())
        #         # Now we have matched our 2 - which is num and 3 which is stack[-1]. We need to match 1         
        #         if pattern == "12":
        #             while stack and stack[-1] >= num:
        #                 backup.append(stack.pop())
        #             if stack and stack[-1] < num:
        #                 return True

        #         stack.extend(backup[::-1])
        #     stack.append(num)
        # return False

        # Optimized solution

        # Use a stack to store possible candidates for 3
        stack = []
        # Variable to store the smallest candidate for '1'
        min_1 = float('-inf')
        
        # Traverse the array from right to left
        for num in reversed(nums):
            if num < min_1:
                return True
            # Pop elements from the stack that are smaller than current num
            while stack and num > stack[-1]:
                min_1 = stack.pop()
            # Push the current number as a potential candidate for '3'
            stack.append(num)
        
        return False
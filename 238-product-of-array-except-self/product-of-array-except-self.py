class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # Solution using separate prefix and postfix arrays
        # if len(nums)==0 or len(nums)==1:
        #     return nums

        # # Initialize arrays
        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)
        # output = [1] * len(nums)

        # # Fill prefix product array
        # prefix[0] = nums[0]
        # for i in range(1, len(prefix)):
        #     prefix[i] = prefix[i-1] * nums[i]
        
        # # Fill postfix product array
        # postfix[-1] = nums[-1]
        # for i in range(len(nums)-2,0,-1):
        #     postfix[i] = postfix[i+1] * nums[i]
        
        # # calculate output using prefix and postfix
        # output[0] = postfix[1]
        # output[-1] = prefix[-2]
        # for i in range(1, len(output)-1):
        #     output[i] = prefix[i-1] * postfix[i+1]

        # return output

        # Solution without separate prefix and postfix array
        if len(nums)==0 or len(nums)==1:
            return nums

        output = [1] * len(nums)
        # calculate prefix and store in the output
        for i in range(1, len(nums)):
            prefix_product = nums[i-1]*output[i-1] 
            output[i] = prefix_product
        
        # calculate output in the reverse order:
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix = postfix * nums[i+1]
            output[i] = postfix * output[i]
            

        return output


        
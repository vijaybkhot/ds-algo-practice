class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prefix = [0]
        for i in range(len(self.array)):
            prefix.append(prefix[-1] + self.array[i])
        return prefix[right+1] - prefix[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        temp_end = nums[n-k:]
        temp_start = nums[:n-k]
        i = 0
        for num in temp_end:
            nums[i] = num
            i += 1
        
        for num in temp_start:
            nums[i] = num
            i += 1
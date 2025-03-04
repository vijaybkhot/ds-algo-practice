class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # Solution using hash map - O(n) extra space
        # # Create a hash-map of index:value as key value pairs
        # index_map = {}
        # for index, num in enumerate(nums):
        #     index_map[index] = num
        
        # for index, num in index_map.items():
        #     new_index = (index + k) % len(nums)
        #     nums[new_index] = num
        
        # # In efficient rotate function
        # def rotate_one_step(arr):
        #     i = len(arr)-1
        #     last_elem = arr[i]
        #     while i > 0:
        #         arr[i] = arr[i-1]
        #         i -= 1
        #     arr[0] = last_elem
        
        # for i in range(k):
        #     rotate_one_step(nums)

        # Simple rotate appraoch
        # Reverse function using two pointer
        def reverse_arr(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        k = k % len(nums)

        n = len(nums)
        reverse_arr(nums, left=0, right=n-1)
        reverse_arr(nums, left=0, right=k-1)
        reverse_arr(nums, left=k, right=n-1)

        
            

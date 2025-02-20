class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # # Insertion Sort time complexity - O(n^2). Space Complexity O(1). In place
        # for i in range(1, len(nums)):
        #     space = i
        #     curr_element = nums[i]
        #     while space > 0 and nums[space-1] > curr_element:
        #         nums[space] = nums[space-1]
        #         space -= 1
        #     nums[space] = curr_element
        # return nums

        # Merge sort: time complexity O(nlogn). space complexity: O(n)


        def merge(left, right):
            sorted_array = []
            i = j = 0

            # Merge the two arrays while maintaining sorted order
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1

            # Add any remaining elements from left or right
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])

            return sorted_array
        
        def merge_sort(arr):
            size = len(arr)
            if size <= 1:
                return arr
            
            mid = size // 2

            left = arr[0:mid]
            right = arr[mid:]

            left = merge_sort(left)
            right = merge_sort(right)
        
            return merge(left, right)
        
        return merge_sort(nums)


        
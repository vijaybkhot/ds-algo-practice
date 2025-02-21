class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # # using insertion sort:
        # for i in range(1, len(nums)):
        #     space = i
        #     curr_elem = nums[space]
        #     while space > 0 and nums[space-1] > curr_elem:
        #         nums[space] = nums[space-1]
        #         space = space - 1
        #     nums[space] = curr_elem
        # return nums

        # Using merge sort: No use here. this is not in place sorting
        # def merge(arr1, arr2):
        #     i, j, sorted_arr = 0, 0, []
        #     while i < len(arr1) and j < len(arr2):
        #         if arr1[i] <= arr2[j]:
        #             sorted_arr.append(arr1[i])
        #             i += 1
        #         else:
        #             sorted_arr.append(arr2[j])
        #             j += 1

        #     sorted_arr.extend(arr1[i:])
        #     sorted_arr.extend(arr2[j:])
        #     return sorted_arr
        
        # def merge_sort(arr):
        #     if len(arr) <= 1:
        #         return arr
        #     mid = len(arr)//2
        #     left = arr[:mid]
        #     right = arr[mid:]
        #     left = merge_sort(left)
        #     right = merge_sort(right)
        #     return merge(left, right)
        

        # # Bucket sort: in place sorting
        # if not nums:
        #     return nums
        # max_elem = max(nums)
        # count = [0] * (max_elem + 1)

        # for num in nums:
        #     count[num] += 1

        # j = 0
        # for i in range(len(count)):
        #     while count[i] > 0:
        #         nums[j] = i  
        #         j += 1
        #         count[i] -= 1
        # return nums

        # One pass partition solution
        l = 0
        r = len(nums)-1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= r:
            if nums[i]==0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -=1
                i -= 1
            i += 1



            


        
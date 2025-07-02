class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def first_occurence(nums, target):
            l, r = 0, len(nums)-1
            first = -1
            # while l <= r:
            #     mid = (l+r)//2
            #     if nums[mid] >= target:
            #         if nums[mid] == target:
            #             first = mid
            #         r = mid-1
            #     else:
            #         l = mid + 1
            # return first
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first

        
        def last_occurence(nums, target):
            last = -1
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        last = mid
                    l = mid +1
                else:
                    r = mid - 1
            
            return last
        
        first, last = first_occurence(nums, target), last_occurence(nums, target)
        return [first, last]










        # # # O(n) solution
        # # result = []
        # # for i in range(len(nums)):
        # #     if nums[i] == target and len(result)== 0:
        # #         result.append(i)
        # #     elif nums[i] == target and len(result)>= 1:
        # #         if(len(result)==1):
        # #             result.append(i)
        # #         else:
        # #             result[1] = i
        
        # # if len(result)== 1:
        # #     if nums[-1] == target:
        # #         result.append(len(nums)-1)
        # #     else:
        # #         result.append(result[0])
        # # if len(result)==0:
        # #     result = [-1, -1]
        
        # # return result

        # # # O(log n) + O(n) solution
        # # low, high = 0, len(nums)-1
        # # target_index = -1
        # # while low <= high:
        # #     mid = (low + high) // 2
        # #     if nums[mid] < target:
        # #         low = mid + 1
        # #     elif nums[mid] > target:
        # #         high = mid - 1
        # #     else:
        # #         target_index = mid
        # #         break
        
        # # if target_index == -1:
        # #     return [-1, -1]
        
        # # low_index, high_index = target_index, target_index
        # # output = [low_index, high_index]
        # # while low_index > -1 and nums[low_index] == target:
        # #     output[0] = low_index
        # #     low_index -= 1
        
        # # while high_index < len(nums) and nums[high_index] == target:
        # #     output[1] = high_index
        # #     high_index += 1
        
        # # return output
        
        # # Optimized O(log n) solution

        # def findFirstOccurrence(nums, target):
        #     low, high = 0, len(nums)-1
        #     first = -1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if nums[mid] >= target:
        #             if nums[mid] == target:
        #                 first = mid
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     return first
        
        # def findLastOccurrence(nums, target):
        #     low, high = 0, len(nums)-1
        #     last = -1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if nums[mid] <= target:
        #             if nums[mid] == target:
        #                 last = mid
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return last
        
        # first = findFirstOccurrence(nums, target)
        # last = findLastOccurrence(nums, target)
        # return [first, last]





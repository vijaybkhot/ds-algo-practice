class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            # If left part is sorted:
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # if right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1











        # # Find the pivot:
        # n = len(nums)
        # l, r = 0, n-1
        # while l < r:
        #     mid = (l+r) // 2

        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # pivot = l
        # # since we have pivot, we find the target in correct portions
        # if nums[pivot] <= target <= nums[n - 1]:
        #     left, right = pivot, n - 1
        # else:
        #     left, right = 0, pivot - 1

        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return -1



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            # If duplicates found:
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                continue
            # If the left part is sorted
            if nums[left] <= nums[mid]:
                # If target lies inside this sorted left part
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right part is sorted:
            elif nums[mid] <= nums[right]:
                # If target lies inside this sorted right part
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
        
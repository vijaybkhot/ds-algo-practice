class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Find pivot:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True

            # If we can't decide the sorted half
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the pivot:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # since we have pivot, we find the target in both portions
        # left portion
        left, right = 0, l-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # if not found, binary search also on right portion
        left, right = l, n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

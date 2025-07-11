class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r, = 0 , n-1
        res = nums[l]
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

        # # res = nums[0]
        # # while l <= r:
        # #     if nums[l] < nums[r]:
        # #         res = min(res, nums[l])
        # #         break

        # #     mid = (l+r)//2
        # #     res = min(res, nums[mid])
        # #     if nums[mid] >= nums[l]:
        # #         l = mid + 1
        # #     else:
        # #         r = mid - 1
        
        # # return res

        # # Pivot solution - Always move to the unsorted portion.
        # while l < r:
        #     mid = (l+r) // 2
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return nums[l]
                
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l <= r:
            mid = (l+r)//2
            left_mid = arr[mid-1] if mid-1 >= 0 else float('-inf')
            right_mid = arr[mid+1] if mid+1 < len(arr) else float('-inf')

            if left_mid < arr[mid] > right_mid:
                return mid
            elif left_mid < arr[mid] < right_mid:
                l = mid+1
            else:
                r = mid-1
        

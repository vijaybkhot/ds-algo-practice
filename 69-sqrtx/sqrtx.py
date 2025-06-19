class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 1, x
        while l <= r:
            mid = (l+r) // 2
            curr_num_square = mid*mid
            if curr_num_square == x:
                return mid
            elif curr_num_square < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
        
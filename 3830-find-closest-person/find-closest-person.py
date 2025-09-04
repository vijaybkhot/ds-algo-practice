class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_a = abs(x-z)
        diff_b = abs(y-z)

        if diff_a > diff_b:
            return 2
        elif diff_a < diff_b:
            return 1
        else:
            return 0
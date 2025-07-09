class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        # while l < r:
        #     if numbers[l]+numbers[r] == target:
        #         return [l+1, r+1]
        #     elif numbers[l]+numbers[r] > target:
        #         r -= 1
        #     else:
        #         l += 1
        
        n = len(numbers)
        for idx, num1 in enumerate(numbers):
            num2 = target - num1
            # search in the rest of the array (right side only)
            j = bisect_left(numbers, num2, idx + 1, n)
            if j < n and numbers[j] == num2:
                return [idx + 1, j + 1]

        
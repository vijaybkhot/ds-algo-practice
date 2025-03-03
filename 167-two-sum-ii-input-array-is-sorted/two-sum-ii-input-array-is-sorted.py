class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_p, right_p = 0, len(numbers)-1

        while left_p < right_p:
            if numbers[left_p] + numbers[right_p] == target:
                break
            elif numbers[left_p] + numbers[right_p] > target:
                right_p -= 1
            elif numbers[left_p] + numbers[right_p] < target:
                left_p += 1
        
        return [left_p+1, right_p+1]

        
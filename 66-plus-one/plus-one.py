class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''.join([str(num) for num in digits])
        new_num = str(int(num_str)+1)
        return [int(str_num) for str_num in new_num]
        
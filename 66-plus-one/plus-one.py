class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num_str = ''.join([str(num) for num in digits])
        # new_num = str(int(num_str)+1)
        # return [int(str_num) for str_num in new_num]
        def dfs(i):
            if i == -1:
                return [1] + digits
            
            else:
                if digits[i] + 1 <= 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
                    return dfs(i-1)
        
        return dfs(len(digits)-1)

        
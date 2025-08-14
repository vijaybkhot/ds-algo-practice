class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_num = float('-inf')
        for i in range(len(num)-2):
            curr_num = num[i:i+3]
            
            num_nums = set(curr_num)
            if len(num_nums) == 1 and int(curr_num) > max_num:
                res = curr_num
                max_num = int(curr_num)
            

        
        return res

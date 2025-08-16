class Solution:
    def maximum69Number (self, num: int) -> int:
        # max_num = num
        # str_num = [char for char in str(num)]

        # for idx, num_char in enumerate(str_num):
        #     if num_char == '6':
        #         str_num[idx] = '9'
        #         max_num = max(max_num, int(''.join(str_num)))
        #         str_num[idx] = '6'
            
        #     if num_char == '9':
        #         str_num[idx] = '6'
        #         max_num = max(max_num, int(''.join(str_num)))
        #         str_num[idx] = '9'
        
        # return max_num
        max_num = num
        str_num = [char for char in str(num)]
        for idx, char_num in enumerate(str_num):
            if char_num == '6':
                str_num[idx] = '9'
                max_num = max(max_num, int(''.join(str_num)))
                break
        
        return max_num

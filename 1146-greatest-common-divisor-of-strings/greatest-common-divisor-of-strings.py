class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # First attempt:
        # if not str1 or not str2:
        #     return ""
        # if len(str1) < len(str2):
        #     str1, str2 = str2, str1
        
       
        # len1,len2 = len(str1), len(str2)
        # gcd = len2
        # while gcd > 0 and (len1%gcd or len2%gcd):
        #     gcd -= 1

        # i, j = 0, 0
        # common_str = ""
        # while j < gcd:
        #     if str1[i] == str2[j]:
        #         common_str += str1[i]
        #         j += 1
        #         i+= 1
        #     else:
        #         break
        
        # gcd_str = len(common_str)
        # if gcd_str == 0:
        #     return ""

        # while j < len(str2):
        #     if str2[j:j+gcd_str] == common_str:
        #         j += gcd_str
        #     else:
        #         return ""
        # i = 0
        # while i < len(str1):
        #     if str1[i:i+gcd_str] == common_str:
        #         i += gcd_str 
        #     else:
        #         return ""
        # return common_str

        # More readable approach
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = math.gcd(len(str1), len(str2))

        return str1[:gcd_length]

        





        




        
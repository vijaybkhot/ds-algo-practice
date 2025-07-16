class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        s_list = s.split(" ")
        # return s_list
        return ' '.join([word for word in s_list[::-1] if word])
            
            
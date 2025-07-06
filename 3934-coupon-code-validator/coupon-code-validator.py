class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        combined_code = [(businessLine[i], code[i], isActive[i]) for i in range(len(code))]
        combined_code.sort()
        res = []
        business_set = set(["electronics", "grocery", "pharmacy", "restaurant"])
        for businessLine, code, isActive in combined_code:
            if not isActive or businessLine not in business_set:
                continue
            isAlNum = True
            for char in code:
                if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
                    isAlNum = False
                    break
            if isAlNum and code:
                res.append(code)
        
        return res
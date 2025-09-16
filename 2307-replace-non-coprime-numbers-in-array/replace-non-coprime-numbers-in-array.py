class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        stack = []
        for num in nums:
            stack.append(num)

            while len(stack) > 1:
                x, y = stack[-2], stack[-1]
                g = gcd(x, y)
                if g == 1:
                    break
                stack.pop()
                stack.pop()
                stack.append(lcm(x,y))
        
        return stack
        
        return stack
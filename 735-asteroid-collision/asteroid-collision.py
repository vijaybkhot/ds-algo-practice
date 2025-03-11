class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # # Working solution without external help
        # stack = []
        
        # for i in range(len(asteroids)):
        #     if not stack:
        #         stack.append(asteroids[i])
        #         continue
        #     num2 = asteroids[i]
        #     if (stack[-1] > 0 and num2 < 0):
        #         num1 = stack.pop()
        #         while True:
        #             if abs(num1) > abs(num2):
        #                 stack.append(num1)
        #                 break
        #             elif abs(num1) < abs(num2):
        #                 if stack and stack[-1] > 0:
        #                     num1 = stack.pop()
        #                     continue
        #                 else:
        #                     stack.append(num2)
        #                     break
        #             else:
        #                 if num1 == num2:
        #                     stack.append(num1)
        #                     stack.append(num2)
        #                 break
        #     else:
        #         stack.append(num2)
        
        # return stack

        # More readabale solution
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack

            

                        

            


            
        
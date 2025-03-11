class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # stack = []
        
        # for i in range(len(asteroids)):
        #     if not stack:
        #         stack.append(asteroids[i])
        #         continue
            
        #     num2 = asteroids[i]
        #     if (stack[-1] > 0 and num2 < 0):
        #         num1 = stack.pop()
        #         if abs(num1) > abs(num2):
        #             while True:
        #             stack.append(num1)
        #         elif abs(num1) < abs(num2):
        #             while True:
        #                 num1 = stack.pop()
        #                 if abs(num1) > abs(num2):
        #                     stack.append(num1)
        #                     break
        #                 elif abs(num1) < abs(num2):
        #                     continue
        #                 else:
        #                     if num1 == num2:
        #                         stack.append(num1)
        #                         stack.append(num2)
        #                     break
        #         else:
        #             continue
        #     else:
        #         stack.append(num2)
        
        # return stack

        stack = []
        
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
                continue
            
            num2 = asteroids[i]
            if (stack[-1] > 0 and num2 < 0):
                num1 = stack.pop()
                while True:
                    if abs(num1) > abs(num2):
                        stack.append(num1)
                        break
                    elif abs(num1) < abs(num2):
                        if stack and stack[-1] > 0:
                            num1 = stack.pop()
                            continue
                        else:
                            stack.append(num2)
                            break
                    else:
                        if num1 == num2:
                            stack.append(num1)
                            stack.append(num2)
                        break
            else:
                stack.append(num2)
        
        return stack

            

                        

            


            
        
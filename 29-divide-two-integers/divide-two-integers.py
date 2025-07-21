class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        quotient = 0
        remainder = 0
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)


        while dividend >= divisor:
            curr_divisor = divisor
            shift = 0
            while (curr_divisor << 1) <= dividend:
                curr_divisor <<= 1
                shift += 1
            dividend -= curr_divisor
            quotient += 1 << shift

        return sign * quotient


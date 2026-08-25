class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        negative = (dividend < 0) != (divisor < 0)

        new_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        while new_dividend >= abs_divisor:
            new_divisor = abs_divisor
            count = 1
            while new_dividend >= (new_divisor << 1):
                new_divisor <<= 1
                count <<= 1
            
            new_dividend -= new_divisor
            quotient += count

        if negative:
            quotient = -quotient
        return max(INT_MIN, min(INT_MAX, quotient))


if __name__ == "__main__":
    s = Solution()
    x = s.divide(42,5)
    print(x)
    y = s.divide(7, -3)
    print(y)
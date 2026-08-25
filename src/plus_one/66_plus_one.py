class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        j = 1

        for i in range(length):
            l = length - i - 1

            if digits[l] + j <= 9:
                digits[l] += j
                return digits

            digits[l] = 0
            j = 1

        return [1] + digits



if __name__ == "__main__":
    digits = [9]
    output = [1,2,4]
    s = Solution()
    print(s.plusOne(digits))


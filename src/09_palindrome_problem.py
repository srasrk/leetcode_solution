class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            x = x // 10
            reversed_num = reversed_num * 10 + digit

        return original == reversed_num

s = Solution()
print(s.isPalindrome(121))  # Returns True
print(s.isPalindrome(-121))  # Returns False
print(s.isPalindrome(10))  # Returns False
print(s.isPalindrome(1)) # Returns True
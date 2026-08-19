from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    digits = [1, 2, 3]
    print(solution.plusOne(digits))
    # Output: [1, 2, 4]

    # Example 2
    digits = [4, 3, 9]
    print(solution.plusOne(digits))
    # Output: [4, 4, 0]

    # Example 3
    digits = [9, 9, 9]
    print(solution.plusOne(digits))
    # Output: [1, 0, 0, 0]
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 2, 2, 3, 3, 4]

    k = solution.removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
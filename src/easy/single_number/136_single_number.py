from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for num, count in map.items():
            if count == 1:
                return num


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    print(solution.singleNumber(nums))  # Output: 4
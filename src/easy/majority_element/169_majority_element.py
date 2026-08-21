import statistics
from typing import List

class Solution:
    def majorityElement_mode(self, nums: List[int]) -> int:
        print(statistics.mode(nums))

    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
                
        return candidate

if __name__ == "__main__":
    solution = Solution()
    nums = [6,6,5]
    result = solution.majorityElement(nums)
    print(f"The majority element in {nums} is: {result}")
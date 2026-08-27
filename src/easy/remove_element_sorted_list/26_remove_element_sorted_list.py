
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for num in nums:
            if num != nums[k]:
                k += 1
                nums[k] = num

        return k+1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,1,2,2,2]
    result = solution.removeDuplicates(nums)
    print(result)  # Output: 5
    print(nums)    # Output: [1, 1, 2]


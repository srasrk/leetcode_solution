from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for num in nums:
            if num in duplicate:
                return True
            
            duplicate[num] = 1

        return False



if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]

    print(s.containsDuplicate(nums))
    nums = [1,2,3,1]
    print(s.containsDuplicate(nums))
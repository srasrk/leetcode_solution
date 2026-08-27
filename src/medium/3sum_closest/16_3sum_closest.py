from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum = 0
        

if __name__ == "__main__":
    s = Solution()

    print(s.threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(s.threeSumClosest([0, 0, 0], 1))        # 0
    print(s.threeSumClosest([1, 1, 1, 0], -100))  # 2

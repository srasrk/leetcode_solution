from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        


        
if __name__ == "__main__":
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)  # [1, 3, 12, 0, 0]

    nums2 = [0, 0, 1]
    #sol.moveZeroes(nums2)
    #print(nums2)  # [1, 0, 0]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = sorted((num, i) for i, num in enumerate(nums))

        start = 0
        end = len(nums) - 1

        while start < end:
            total = nums[start][0] + nums[end][0]

            if total == target:
                return [nums[start][1], nums[end][1]]
            elif total < target:
                start += 1
            else:
                end -= 1

        return []

    def twoSum_optimal(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_to_index:
                return [num_to_index[difference], i]
            num_to_index[num] = i

if __name__ == "__main__":
    nums = [-3, -2, -4]
    target = -6

    s = Solution()
    print(s.twoSum_optimal(nums, target))
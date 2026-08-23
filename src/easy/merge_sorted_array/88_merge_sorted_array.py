class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        #for i in range(m, len(nums1)):
        #    nums1[i] = nums2[i - m]
        
        #nums1[i].sort()
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j -=1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    
if __name__ == "__main__":
    s = Solution()
    
    nums1 = [1, 3, 5, 0, 0, 0]
    nums2 = [2, 4, 6]

    s.merge(nums1, 3, nums2, 3)

    print(nums1)

    nums1 = [1, 2, 4, 5, 0, 0, 0]
    nums2 = [3, 6, 7]

    s.merge(nums1, 4, nums2, 3)

    print(nums1)
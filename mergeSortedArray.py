class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(n == 0):
            return
        else:
            a = 0
            b = 0
            while(b <= n - 1):
                if(nums1[a] < nums2[b] and a < m + b):
                    a += 1
                elif(nums1[a] >= nums2[b] or a == m + b):
                    c = nums1[a]
                    nums1[a] = nums2[b]
                    nums1.insert(a + 1, c)
                    nums1.pop()
                    a += 1
                    b += 1

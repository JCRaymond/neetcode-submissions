class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 == 0:
            m = n1//2
            if n1 % 2 == 0:
                return (nums1[m-1] + nums1[m])/2
            return nums1[m]

        print(nums1)
        print(nums2)
        half = (n1 + n2)//2

        l = 0
        r = n1

        m1 = (l + r)//2
        m2 = half - m1
        while r - l > 1:
            if nums1[m1-1] > nums2[m2]:
                r = m1
            elif nums2[m2-1] > nums1[m1]:
                l = m1
            else:
                break
            m1 = (l + r)//2
            m2 = half - m1
        
        if m1 == n1:
            if (n1 + n2)%2 == 0:
                return (nums1[-1] + nums2[0])/2
            return nums2[0]
        if m2 == n2:
            if (n1 + n2)%2 == 0:
                return (nums2[-1] + nums1[0])/2
            return nums1[0]
        
        if (n1 + n2)%2 == 0:
            return (max(nums1[m1-1], nums2[m2-1]) + min(nums1[m1], nums2[m2]))/2
        
        return min(nums1[m1], nums2[m2])
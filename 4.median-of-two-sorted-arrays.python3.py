class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        start, end = 0, m

        while start <= end:
            i = (start + end) // 2
            j = (m + n + 1) // 2 - i

            if i != 0 and j != n and nums1[i - 1] > nums2[j]:
                end = i - 1
            elif j != 0 and i != m and nums2[j - 1] > nums1[i]:
                start = i + 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2:
                    return maxLeft

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                return (maxLeft + minRight) / 2

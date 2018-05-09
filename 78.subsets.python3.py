class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(results, sub, start, nums):
            if start == len(nums):
                results.append(sub.copy())
            else:
                sub.append(nums[start])
                backtrack(results, sub, start + 1, nums)
                sub.pop()
                backtrack(results, sub, start + 1, nums)

        results = []
        backtrack(results, [], 0, nums)

        return results

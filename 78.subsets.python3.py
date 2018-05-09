class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(results, sub, start, nums):
            if start == len(nums):
                results.append(sub.copy())  # 格外注意不能写成 sub
            else:
                sub.append(nums[start])
                backtrack(results, sub, start + 1, nums)
                sub.pop()
                backtrack(results, sub, start + 1, nums)

        results = []
        backtrack(results, [], 0, nums)

        return results

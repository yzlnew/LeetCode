class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows:
            return []

        res = [[1]]

        for i in range(numRows-1):
            res.append(
                list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))

        return res

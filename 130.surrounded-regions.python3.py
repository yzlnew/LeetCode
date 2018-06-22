class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        boundary = [loc for i in range(m) for loc in (
            (i, 0), (i, n - 1))] + [loc for i in range(n) for loc in ((0, i), (m - 1, i))]

        while boundary:
            x, y = boundary.pop()

            if x in range(m) and y in range(n) and board[x][y] == 'O':
                boundary += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                board[x][y] = 'M'

        for row in board:
            for col, val in enumerate(row):
                if val == 'M':
                    row[col] = 'O'
                else:
                    row[col] = 'X'

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        self.dfs(s, path, res)

        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)

            return

        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path + [s[:i]], res)

def main():
    s = Solution()
    s.partition('aab')

if __name__ == '__main__':
    main()
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = [i.lower() for i in s if i.isalnum()]
        return new_s == new_s[::-1]

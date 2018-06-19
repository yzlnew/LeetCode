class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        wordDict.remove(endWord)
        step = 0

        while s1 and s2:
            step = step + 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()

            for word in s1:
                new_words = [word[:i] + t + word[i + 1:] for t in
                             string.ascii_lowercase for i in range(l)]

                for new_word in new_words:
                    if new_word in s2:
                        return step + 1

                    if new_word not in wordDict:
                        continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        l = len(beginWord)

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length
            new_words = [word[:i] + t + word[i + 1:] for t in
                         string.ascii_lowercase for i in range(l)]

            for word in new_words:
                if word in wordSet:
                    wordSet.remove(word)
                    queue.append([word, length + 1])

        return 0

    def ladderLength_bi(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        wordSet.remove(endWord)
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

                    if new_word not in wordSet:
                        continue
                    wordSet.remove(new_word)
                    s.add(new_word)
            s1 = s

        return 0

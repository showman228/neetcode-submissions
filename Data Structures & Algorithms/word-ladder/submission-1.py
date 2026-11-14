class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        words = set(wordList)
        res = 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for char in range(97, 123):
                        if chr(char) == word[i]:
                            continue
                        nei = word[:i] + chr(char) + word[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0

        
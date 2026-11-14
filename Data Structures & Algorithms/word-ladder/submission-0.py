class Solution:
    def checkVal(self, curWord: str, wordList: List[str]) -> List[str]:
        
        lst = []
        for word in wordList:
            p = 0
            check = 0
            while p < len(curWord):
                if curWord[p] != word[p]:
                    check += 1
                p += 1
            if check == 1:
                lst.append(word)
        return lst


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        count = 1
        q = deque([word for word in self.checkVal(beginWord, wordList)])

        while q:
            curWord = q.popleft()

            if curWord == endWord:
                return count
            
            variants = [word for word in self.checkVal(curWord, wordList)]
            for word in variants:
                q.append(word)

            count += 1

        return count
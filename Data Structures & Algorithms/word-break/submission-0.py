from functools import lru_cache
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @lru_cache(None)
        def dfs(i: int):
            
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False

        return dfs(0)
            
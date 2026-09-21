class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win = [] # окно

        for right in range(len(s2)):
            win.append(s2[right])
            while len(win) > len(s1):
                win.pop(0)
            word = "".join(win)
            if sorted(word) == sorted(s1):
                return True
        
        return False
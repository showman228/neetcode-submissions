class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[right]) - ord('a')
            s2_count[idx] += 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] + 1 == s2_count[idx]:
                matches -= 1

            idx = ord(s2[left]) - ord('a')
            s2_count[idx] -= 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] - 1 == s2_count[idx]:
                matches -= 1

            left += 1


        return matches == 26



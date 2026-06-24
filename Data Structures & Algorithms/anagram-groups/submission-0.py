class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list) # sorted value: [anagrams]

        for elem in strs:
            sortedS = "".join(sorted(elem))
            dct[sortedS].append(elem)

        return list(dct.values())


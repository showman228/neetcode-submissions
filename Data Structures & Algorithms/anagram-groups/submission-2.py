class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hs = defaultdict(list)
        for string in strs:
            string_sort = "".join(sorted(string))
            hs[string_sort].append(string)


        return [val for val in hs.values()]
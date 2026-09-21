class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = list()
        for elem in nums1:
            new_list.append(elem)
        for elem in nums2:
            new_list.append(elem)
        
        new_list.sort()

        check = len(new_list) % 2 != 0

        if check:
            mid = len(new_list) // 2
            return new_list[mid]
        
        l = 0
        r = len(new_list) - 1
        m = (l + r) // 2

        return (new_list[m] + new_list[m + 1]) / 2

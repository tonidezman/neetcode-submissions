def get_distinct(nums1, nums2) -> list[int]:
    set2 = set(nums2)
    res = []
    for num in set(nums1):
        if num not in set2:
            res.append(num)
    return res


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = get_distinct(nums1, nums2)
        second = get_distinct(nums2, nums1)
        return [first, second]
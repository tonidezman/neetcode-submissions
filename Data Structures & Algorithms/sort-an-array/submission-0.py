class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(l: int, r: int) -> None:
            if l == r:
                return
            m = l + (r - l) // 2
            mergeSort(l, m)
            mergeSort(m+1, r)

            merge(l, r)

        def merge(l: int, r: int) -> None:
            mid = l + (r - l) // 2
            left, right = nums[l:mid+1], nums[mid+1:r+1]
            p1 = p2 = 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    nums[l] = left[p1]
                    p1 += 1
                else:
                    nums[l] = right[p2]
                    p2 += 1
                l += 1
            
            while p1 < len(left):
                nums[l] = left[p1]
                p1 += 1
                l += 1

            while p2 < len(right):
                nums[l] = right[p2]
                p2 += 1
                l += 1

        mergeSort(l=0, r=len(nums)-1)
        return nums

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(curr[:])
                return
            dfs(i+1)
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
        dfs(i=0)
        return res
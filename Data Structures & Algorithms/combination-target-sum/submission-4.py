class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i: int, total: int) -> None:
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()
            dfs(i+1, total)
        dfs(i=0, total=0)
        return res
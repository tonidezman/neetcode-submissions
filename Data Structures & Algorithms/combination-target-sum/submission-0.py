class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i: int, curr, total) -> None:
            if total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i+1, curr, total)
        dfs(i=0, curr=[], total=0)
        return res
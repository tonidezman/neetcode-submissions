class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        self.dfs(nums, res, curr, i=0, total=0, target=target)
        return res

    def dfs(self, nums, res, curr, i, total, target):
        if total == target:
            res.append(curr[:])
            return
        if total > target or i >= len(nums):
            return
        curr.append(nums[i])
        self.dfs(nums, res, curr, i, total+nums[i], target)
        curr.pop()
        self.dfs(nums, res, curr, i+1, total, target)
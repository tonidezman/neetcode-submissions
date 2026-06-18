class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let seen = {}
        for (let i=0; i < nums.length; i++) {
            let num = nums[i]
            let other_num = target - num
            if (other_num in seen) {
                return [seen[other_num], i]
            }
            seen[num] = i
        }
    }
}

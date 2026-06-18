class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i=0; i<nums.size(); i++) {
            int other = target - nums[i];
            if (seen.count(other)) {
                return vector<int> {seen[other], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};

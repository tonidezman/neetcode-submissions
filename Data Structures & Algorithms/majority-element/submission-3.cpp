class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int num = nums[0];

        for (int i=1;i<nums.size();i++) {
            if (num == nums[i]) count += 1;
            else {
                count -= 1;
                if (count == 0) {
                    count = 1;
                    num = nums[i];
                }
            }
        }
        return num;
    }
};
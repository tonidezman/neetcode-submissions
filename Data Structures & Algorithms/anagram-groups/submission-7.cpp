class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hsh;
        for (string word : strs) {
            string wrd = word;
            sort(wrd.begin(), wrd.end());
            hsh[wrd].push_back(word);
        }
        vector<vector<string>> res;
        for (const auto& [key, arr] : hsh) {
            res.push_back(arr);
        }
        return res;
    }
};

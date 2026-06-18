class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string res = strs[0];
        for (int i=1;i<strs.size();i++) {
            string curr = "";
            string word = strs[i];
            for (int j=0;j<word.length();j++) {
                if (j == res.length() || word[j] != res[j]) {
                    break;
                } else {
                    curr += word[j];
                }
            }
            if (curr.length() < res.length()) res = curr;
        }
        return res;
    }
};
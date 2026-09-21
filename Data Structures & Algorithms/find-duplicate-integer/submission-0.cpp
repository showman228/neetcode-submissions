class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int, int> hs;

        for (const auto elem : nums) {
            if (hs[elem]) {
                return elem;
            }
            else {
                hs[elem]++;
            }
        }
        return -1;
    }
};

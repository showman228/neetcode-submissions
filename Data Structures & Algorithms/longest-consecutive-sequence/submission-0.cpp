class Solution {
public:
    vector<int> SortVec(vector<int>& v){
        sort(v.begin(), v.end());
        auto it = unique(v.begin(), v.end());
        v.erase(it, v.end());
        return v;
    }

    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }
        else if (nums.size() == 1){
            return 1;
        }
        else {
            int count = 1;
        vector<int> v;
        nums = SortVec(nums);
        for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] + 1 == nums[i + 1] ) {
            count++;
        }
        else {
            v.push_back(count);
            count = 1;
            }
        }
        v.push_back(count);
        int max_elem = 0;
        for (const auto& num : v) {
            if (max_elem < num) {
                max_elem = num;
            }
        }
            return max_elem;
        }
    }
};

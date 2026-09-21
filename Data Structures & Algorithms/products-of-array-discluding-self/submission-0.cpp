class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    size_t sz = nums.size();
    vector<int> ans;
    for (int i = 0; i < sz; i++) {
        int prod = 1;
        for (int j = 0; j < sz; j++) {
            if (i != j) {
                prod *= nums[j];
            }
        }
        ans.push_back(prod);
    }
    return ans;
}
};

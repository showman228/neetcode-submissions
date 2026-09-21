class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

    sort(nums.begin(), nums.end());

    int left;
    int right;
    int total;

    vector<vector<int>> sp;

    for (int i = 0; i < nums.size(); i++) {

        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        left = i + 1;
        right = nums.size() - 1;
        total = 0;

        while (left < right){
            total = nums[left] + nums[right] + nums[i];

            if (total == 0){
                vector<int> temp = {nums[left], nums[i], nums[right]};
                sp.push_back(temp);
                left++;
                while (nums[left] == nums[left - 1] && left < right) {
                    left++;
                }
            }
            else if (total < 0) {
                left++;
            }
            else if (total > 0) {
                right--;
            }
        }
    }
        return sp;
    }
};

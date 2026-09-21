class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int out_left = 0;
        int out_right = matrix.size() - 1;

        while (out_left <= out_right) {
            int mid = (out_left + out_right) / 2;

            if (matrix[mid][0] < target && matrix[mid][matrix[mid].size()- 1] > target) {
                break;
            }
            else if (matrix[mid][0] > target) {
                out_right = mid - 1;
            }
            else {
                out_left = mid + 1;
            }
        }

        vector<int> sp = matrix[(out_left + out_right) / 2];

        int left = 0;
        int right = sp.size() - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (sp[mid] == target) {
                return true;
            }
            else if (sp[mid] > target) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return false;
    }
};

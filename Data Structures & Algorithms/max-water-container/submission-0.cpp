class Solution {
public:
    int GetMin(int a, int b){
    if (a > b) {
        return b;
    }
    return a;
}

int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int res = 0;

    while (left < right) {

        int distance = right - left;
        int minValue = GetMin(height[left], height[right]);
        int current_area = distance*minValue;

        if (current_area > res) {
            res = current_area;
        }
        if (height[left] < height[right]){
            left++;
        }
        else if (height[left] > height[right]) {
            right--;
        }
        else {
            left++;
        }
    }
    return res;
}
};

class Solution {
public:
    bool isPalindrome(string s) {
        
    string str = "";    

    if (s.size() == 0 || s.size() == 1){
        return true;
    }

    for(const auto& elem : s){
        if (isalnum(elem)){
            str += tolower(elem);
        }
    }

    int left = 0;
    int right = str.size() - 1;

    while (left < right) {
        if (str[left] != str[right]){
            return false;
        }    
        left++;
        right--;
    }
    return true;
}
};

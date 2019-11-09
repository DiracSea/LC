# include <vector>
using std::vector;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        
        return i;
    }
    int removeElement1(vector<int>& nums, int val) {
        int n = nums.size();
        auto it = nums.begin();
        
        int removeCount = 0;
        while (it!=nums.end()) {
            if (*it==val) {
                nums.erase(it);
                removeCount++;
            } else {
                it++;
            }
        }
        
        return n-removeCount;
    }  
};
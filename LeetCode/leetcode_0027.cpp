#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int s = nums.size();
        int i = 0;
        while (i < s) {
            if (nums[i] == val) {
                nums[i] = nums[s - 1];
                s--;
            }
            else {
                i++;
            }
        }
        return s;
    }
};

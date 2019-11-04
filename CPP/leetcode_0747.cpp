#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int size = nums.size();
        if (size <= 0) {
            return -1;
        }
        if (size == 1) {
            return 0;
        }
        int i = 0;
        int max = 0;
        int second = 0;
        int i_max = 0;
        for (int i = 0; i < size; i++) {
            if (i < size) {
                if (nums[i] > max) {
                    second = max;
                    i_max = i;
                    max = nums[i];
                }
                else if (nums[i] > second) {
                    second = nums[i];
                }
            }
        }
        if (max >= second * 2) {
            return i_max;
        }
        else {
            return -1;
        }  
    }
};
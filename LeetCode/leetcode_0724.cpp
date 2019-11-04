#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int size = nums.size();

        int sum_of_elems = 0;
        for (auto& n : nums) {
            sum_of_elems += n;
        }
        int sum_of_left = 0;
        int i = 0;
        while (i < size) {
            if (sum_of_left == sum_of_elems - nums[i] - sum_of_left) {
                return i;
            }
            sum_of_left += nums[i];
            i++;
        }

        return -1;
    }
};
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        int i = 0;
        int n = 0;
        digits.insert(digits.begin(), 0);
        digits[size] += 1;
        for (i = size; i > 0; --i) {
            n = digits[i];
            if (n >= 10) {
                digits[i] = n % 10;
                digits[i - 1] += 1;
            }
        }
        if (digits[0] == 0) {
            auto it = digits.begin();
            digits.erase(it);
        }
        return digits;
    }
};
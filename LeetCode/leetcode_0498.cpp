#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int rows = matrix.size();
        if (rows <= 0) {
            return result;
        }
        int cols = matrix[0].size();

        int epochs = rows + cols - 1;
        int epoch = 0;
        int flag = 1;
        int row = 0;
        int col = 0;
        while (epoch < epochs) {
            if (flag == 1) {
                row = epoch;
                col = 0;
                while (row >= 0) {
                    if (0 <= row && row < rows && 0 <= col && col < cols) {
                        result.push_back(matrix[row][col]);
                    }
                    row -= 1;
                    col += 1;
                }
            }
            else {
                row = 0;
                col = epoch;
                while (col >= 0) {
                    if (0 <= row && row < rows && 0 <= col && col < cols) {
                        result.push_back(matrix[row][col]);
                    }
                    row += 1;
                    col -= 1;
                }
            }
            epoch += 1;
            flag *= -1;
        }
        return result;
    }
};
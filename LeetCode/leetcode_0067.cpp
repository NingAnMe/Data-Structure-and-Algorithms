#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        if (b.length() > a.length()) {
            string temp = a;
            a = b;
            b = temp;
        }
        int i = a.length() - 1;
        int j = b.length() - 1;
        bool flag = false;
        for (i; i >= 0; i--) {
            if (j >= 0) {
                if (flag == true) {
                    if (a[i] == b[j]) {
                        a[i] = '1';
                        if (b[j] == '0') {
                            flag = false;
                        }
                    }
                    else {
                        a[i] = '0';
                    }
                }
                else {
                    if (a[i] == b[j]) {
                        a[i] = '0';
                        if (b[j] == '1') {
                            flag = true;
                        }
                    }
                    else {
                        a[i] = '1';
                    }
                }
                j--;
            }
            else {
                if (flag == true) {
                    if (a[i] == '1') {
                        a[i] = '0';
                    }
                    else {
                        a[i] = '1';
                        flag = false;
                    }
                }
                else {
                    break;
                }
            }
        }
        if (flag == true) {
            a.insert(0, "1");
        }
        return a;
    }
};
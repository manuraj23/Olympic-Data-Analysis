#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool fun(string str) {
        int n = str.size();
        if (n < 3) {
            return false;
        }

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                int a = stoi(str.substr(i, j - i));
                for (int k = j + 1; k < n; k++) {
                    int b = stoi(str.substr(j, k - j));
                    int idx = k;
                    while (true) {
                        int c = a + b;
                        string c_str = to_string(c);
                        if (idx + c_str.size() > n || str.substr(idx, c_str.size()) != c_str) {
                            break;
                        }
                        idx += c_str.size();
                        a = b;
                        b = c;
                        if (idx == n)
                            return true;
                    }
                }
            }
        }
        return false;
    }
};


int main() {
    Solution sol;
    
    // Test cases
    string test1 = "112358";
    string test2 = "199100199";
    string test3 = "14748";

    // Testing the function
    cout << "Result for test1: " << sol.fun(test1) << endl; // Should output: 1 (true)
    cout << "Result for test2: " << sol.fun(test2) << endl; // Should output: 1 (true)
    cout << "Result for test3: " << sol.fun(test3) << endl; // Should output: 1 (true)    
    
    return 0;
}
